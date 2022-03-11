# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Spec of algorithm."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from logger import logger

class AlgorithmsFactory(object):
    """ simple factory for algorithm
    """
    @staticmethod
    def build_algorithm(algo):
        algorithms = {
           "gang": GangSchedulingAlgo,
           "drf": DRFSchedulingAlgo,
           "fifo": FIFOSchedulingAlgo
        }

        return algorithms[algo](name = "{}".format(algo))


class Algorithm(object):
    """Specification for scheduling algorithm."""

    def __init__(self, name):
        """
        Args:
            name: algorithm name
        """
        self._name = name

    @property
    def name(self):
        return self._name

    def schedule_job(self, job_queue, cluster):
        return 


class GangSchedulingAlgo(Algorithm):
    """Specification for gang scheduling algorithm."""

    def __init__(self, name):
        """
        Args:
            name: node name
        """
        super(GangSchedulingAlgo, self).__init__(name)
        self._name = name

    @property
    def name(self):
        return self._name

    def schedule_job(self, job_queue, cluster):
        # TODO
        return 


class FIFOSchedulingAlgo(Algorithm):
    """Specification for First On First Out (FIFO) algorithm."""

    def __init__(self, name):
        """
        Args:
            name: node name
        """
        super(FIFOSchedulingAlgo, self).__init__(name)
        self._name = name

    @property
    def name(self):
        return self._name

    def schedule_single_job(self, job_queue, cluster):
        logger.debug("name {}, job_queue {}, nodes count {}".format(self._name, \
                     job_queue, cluster.nodes_count))

        if len(job_queue) == 0:
            # queue is empty
            return
        else:
            # pop first job
            job = job_queue.pop(0)

        # sort based on free resources
        node_list = sorted(cluster.node_list, \
                            key = lambda node : node.free_gpus_count)
        
        node_candidates = []
        
        for i in range(job.num_tasks):
            for node in node_list:
                if node.contains_sufficient_resources(job.task_resouce_spec):
                    node.allocate_task(job.task_resouce_spec, job.name)
                else:
                    continue
        
        # job task not allocated. assume gang scheduling release resources
        if job.allocated_task_num < job.num_tasks:
            job.release_job(cluster)
            job_queue.append(job) # append to queue tail
            return False 

        return True

    def schedule_jobs(self, jobs, cluster):
        return 


class DRFSchedulingAlgo(Algorithm):
    """Specification for DRF algorithm."""

    def __init__(self, name):
        """
        Args:
            name: node name
        """
        super(DRFSchedulingAlgo, self).__init__(name)
        self._name = name

    @property
    def name(self):
        return self._name

    def schedule_single_job(self, job_queue, cluster):
        logger.debug("name {}, job_queue {}, nodes count {}".format(self._name, \
                     job_queue, cluster.nodes_count))
        return 
