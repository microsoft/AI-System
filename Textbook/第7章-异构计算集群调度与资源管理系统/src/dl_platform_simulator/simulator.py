# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Simulator for DL platform.

CMD example: 
python simulator.py --trace_path ../../philly-traces/trace-data-sample
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import yaml
from event import *
import argparse
import json
import pandas as pd 
from cluster import *
from node import *
from job import *
from event import *
from datetime import datetime
from logger import logger
from utils import *
from scheduler import Scheduler
from global_clock import GlobalClock

parser = argparse.ArgumentParser(description='Process configurations.')
parser.add_argument('--trace_path', type=str, 
                    default=r'./', help='input trace data path')
parser.add_argument('--sched_algo', type=str, 
                    default=r'fifo', help='schedule algorithm')

class Simulator(object):
    """Deep learning platform simulator."""

    def __init__(self, name, args):
        """
        Args:
            name: node name
        """
        self._name = name
        self._args = args
        # store events of job in, job release, monitor profile, etc.
        self._event_queue = [] 
        # add job when no free resources
        self._pending_job_queue = []
        # jobs
        self._jobs = []
        self._bad_jobs = []
        self._scheduler = Scheduler(name = "scheduler1", algorithm = args.sched_algo)
        self._global_clock = None

    @property
    def name(self):
        return self._name

    def simulate(self):
        """Simulate events."""

        # state machine of scheduler
        while len(self._event_queue) != 0:
            logger.debug("pop event from event queue")
            event = self._event_queue.pop(0)

            def submit_job():       
                """
                    submit job and trigger scheduling
                """                         
                logger.debug('This is the {}'.format(event))
                self._pending_job_queue.append(event.job)
                
                if self._scheduler.schedule_job(self._pending_job_queue, \
                                                self._cluster):
                    release_event = ReleaseJobEvent(job, job.job_lifetime \
                                                    + self._global_clock) 
                    self._event_queue.append(release_event)
                    # need to select more efficient data structure
                    self._event_queue = sorted(self._event_queue, \
                                               key = lambda event : \
                                                   event.timestamp)
            def release_job():                        
                """
                    free resource and trigger scheduling
                """    
                logger.debug('This is the {}'.format(event))
                self._scheduler.release_job(event.job, self._cluster)
                self._scheduler.schedule_job(self._pending_job_queue, \
                                             self._cluster)

            def profile_cluster():                            
                logger.debug('This is the {}'.format(event))


            def default():                          
                logger.debug('No such case')

            switch = {"submit_job": submit_job,
                     "release_job": release_job,
                     "profile_cluster": profile_cluster
                     }

            logger.debug(event.type)
            switch.get(event.type, default)()    
            self._global_clock = event.timestamp # update the global event 
        return 

    def build_clusters(self, machines):
        '''
            create cluster machines object
        '''
        self._cluster = Cluster(name = "cluster1")
        
        for index, machine in machines.iterrows():
            logger.debug(machine)
            node = Node(name = machine["machineId"], \
                        gpus_count = machine["_number_of_GPUs"], \
                        gpus_spec = "P100")
            self._cluster.add_node(node)
        
        logger.debug("node counts {}".format(self._cluster.nodes_count))
    
    def build_jobs(self, jobs):
        '''
            create cluster jobs object
        '''
        jobs_list = [Job(**job) for job in jobs]
        self._jobs = jobs_list
            
    def build_job_events(self):
        for job in self._jobs:
            if job.submitted_time != job.released_time and job.released_time is \
                not None and job.submitted_time is not None:
                submit_event = SubmitJobEvent(job) 
                self._event_queue.append(submit_event)

            else:
                self._bad_jobs.append(job)

        self._event_queue = sorted(self._event_queue, \
                                   key = lambda event : event.timestamp)
        if self._global_clock == None:
            self._global_clock = GlobalClock(self._event_queue[0].timestamp)

    def print_yml(self, config):
        '''
            for debugging
        '''
        for key, value in config.items():
            logger.debug(key)
            logger.debug(value)
            for k, v in value.items():
                logger.debug(k)
                logger.debug(v)
                    
    def build(self, config_path, trace_path):
        # construct cluster and event queue
        cluster_machine_list_path = "{}/cluster_machine_list".format(trace_path) 
        cluster_jobs_path = "{}/cluster_job_log".format(trace_path) 
        cluster_machine_list_path = "{}/cluster_machine_list".format(trace_path) 
        # preprocess data

        with open(config_path) as f:
            with open(cluster_machine_list_path) as cml_f:
                with open(cluster_jobs_path) as cj_f:
                    config = yaml.load(f)
                    machines = pd.read_csv(cml_f)
                    # rm blank in col name
                    machines.columns = [col.replace(' ', '_') \
                                        for col in machines.columns]
                    jobs = json.load(cj_f)
                    # EDA 
                    logger.debug(machines.info())
                    logger.debug(machines.describe())
                    logger.debug(jobs[0])
                    logger.debug(config["clusters"])
                    # build cluster and job
                    #self.print_yml(config)
                    self.build_clusters(machines)
                    self.build_jobs(jobs)
                    self.build_job_events()

        # start simulation
        self.simulate
        return

def main():
    args = parser.parse_args()
    logger.debug("start main function")
    trace_path = args.trace_path
    simualtor = Simulator(name = "prod_cluster", args = args)
    simualtor.build(config_path = "config/config1.yml", trace_path = trace_path)
    simualtor.simulate()
  
if __name__=="__main__":
    main()
