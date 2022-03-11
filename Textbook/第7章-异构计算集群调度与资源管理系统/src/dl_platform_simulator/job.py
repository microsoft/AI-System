# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Copyright 2019 The msr-fiddle Team

This file is adapted from https://github.com/msr-fiddle/philly-traces
"""

"""Spec of job."""

import csv
import datetime
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import random

LOGDIR = '../trace-data'
DATE_FORMAT_STR = '%Y-%m-%d %H:%M:%S'
MINUTES_PER_DAY = (24 * 60)
MICROSECONDS_PER_MINUTE = (60 * 1000)

def parse_date(date_str):
    """Parses a date string and returns a datetime object if possible.
    
       Args:
           date_str: A string representing a date.
        
       Returns:
           A datetime object if the input string could be successfully
           parsed, None otherwise.
    """
    if date_str is None or date_str == '' or date_str == 'None':
        return None
    return datetime.datetime.strptime(date_str, DATE_FORMAT_STR)

def timedelta_to_minutes(timedelta):
    """Converts a datetime timedelta object to minutes.
    
       Args:
           timedelta: The timedelta to convert.
           
       Returns:
           The number of minutes captured in the timedelta.
    """
    minutes = 0.0
    minutes += timedelta.days * MINUTES_PER_DAY
    minutes += timedelta.seconds / 60.0
    minutes += timedelta.microseconds / MICROSECONDS_PER_MINUTE
    return minutes

def round_to_nearest_minute(t):
    """Rounds a datetime object down to the nearest minute.
    
       Args:
           t: A datetime object.
           
        Returns:
            A new rounded down datetime object.
    """
    return t - datetime.timedelta(seconds=t.second, microseconds=t.microsecond)

def add_minute(t):
    """Adds a single minute to a datetime object.
    
       Args:
           t: A datetime object.
           
        Returns:
            A new datetime object with an additional minute.
    """
    return t + datetime.timedelta(seconds=60)

class Job:
    """Encapsulates a job."""
    
    def __init__(self, status, vc, jobid, attempts, submitted_time, user):
        """Records job parameters and computes key metrics.
        
           Stores the passed in arguments as well as the number of GPUs
           requested by the job. In addition, computes the queueing delay
           as defined as the delta between the submission time and the start
           time of the first attempt. Finally, computes run time as defined
           as the delta between the initial attempt's start time and the last
           attempt's finish time.
           
           NOTE: Some jobs do not have any recorded attempts, and some attempts
           have missing start and/or end times. A job's latest attempt having no
           end time indicates that the job was still running when the log data
           was collected.
   
           Args:
               status: One of 'Pass', 'Killed', 'Failed'.
               vc: The hash of the virtual cluster id the job was run in.
               jobid: The hash of the job id.
               attempts: A list of dicts, where each dict contains the following keys:
                   'start_time': The start time of the attempt.
                   'end_time': The end time of the attempt.
                   'detail': A list of nested dicts where each dict contains 
                             the following keys:
                        'ip': The server id.
                        'gpus': A list of the GPU ids allotted for this attempt.
                submitted_time: The time the job was submitted to the queue.
                user: The user's id.            
        """
        self._status = status
        self._vc = vc
        self._jobid = jobid
        for attempt in attempts:
            attempt['start_time'] = parse_date(attempt['start_time'])
            attempt['end_time'] = parse_date(attempt['end_time'])
        self._attempts = attempts
        self._submitted_time = parse_date(submitted_time)
        self._released_time = self._submitted_time

        for i in range(len(attempts)):
            if attempts[len(attempts) - 1 - i]['end_time'] != "None":
                self._released_time = attempts[len(attempts) - 1 - i]['end_time']
                break

        self._user = user
        
        if len(self._attempts) == 0:
            self._num_gpus = None
            self._run_time = None
            self._queueing_delay = None
        else:
            self._num_gpus = sum([len(detail['gpus']) for detail in self._attempts[0]['detail']])
            if self._attempts[0]['start_time'] is None:
                self._run_time = None
                self._queueing_delay = None
            else:
                if self._attempts[-1]['end_time'] is None:
                    self._run_time = None
                else:
                    self._run_time = \
                        timedelta_to_minutes(self._attempts[-1]['end_time'] -
                                             self._attempts[0]['start_time'])
                self._queueing_delay = \
                    timedelta_to_minutes(self._attempts[0]['start_time'] -
                                         self._submitted_time)
        
        # simple model, assume one task one GPU 
        self._num_tasks = self._num_gpus
        # random init per CPU request (the value is a multiple of the number of GPUs)
        cpu_count_size_set = {1,2,3,4,5,6,7,8}

        if self._num_gpus is None:
            self._num_gpus = 0

        self._per_task_cpus = random.choice(tuple(cpu_count_size_set))
        self._cpus = self._per_task_cpus * self._num_tasks
        
        host_mem_size_set_mb = {512,1024,2048,4096,8192,16384} # MB
        # random init task host memory request
        self._per_task_mems = random.choice(tuple(host_mem_size_set_mb)) 
        self._host_mems_mb = self._per_task_mems * self._num_tasks

        self._allocated_node_dic = {} # node name -> task counts
        self._allocated_task_num = 0 

    @property
    def status(self):
        return self._status
    
    @property
    def vc(self):
        return self._vc
    
    @property
    def jobid(self):
        return self._jobid
    
    @property
    def attempts(self):
        return self._attempts
    
    @property
    def submitted_time(self):
        return self._submitted_time

    @property
    def released_time(self):
        return self._released_time
 
    @property
    def job_lifetime(self):
        return self._released_time - self._submitted_time

    @property
    def user(self):
        return self._user
    
    @property
    def num_gpus(self):
        return self._num_gpus
    
    @property
    def num_tasks(self):
        return self._num_tasks

    @property
    def task_resouce_spec(self):
        return (1, self._per_task_cpus, self._per_task_mems) # GPU, cpu, mem

    @property
    def queueing_delay(self):
        return self._queueing_delay
    
    @property
    def run_time(self):
        return self._run_time

    @property
    def cpus(self):
        return self._cpus

    @property
    def host_mems_mb(self):
        return self._host_mems_mb

    def allocate_one_task_to_node(self, node):
        if node.name in self._allocated_node_dic:
            self._allocated_node_dic[node.name]["task_count"] += 1
        else:
            self._allocated_node_dic[node.name] = {"task_count": 1, "node": node}

        self._allocated_task_num = +1

    def release_all_tasks(self, cluster):
        for node_name in self._allocated_node_dic:
            node = self._allocated_node_dic[node_name]["node"]
            for i in range(self._allocated_node_dic[node_name]["task_count"]):
                node.release_task(self)
