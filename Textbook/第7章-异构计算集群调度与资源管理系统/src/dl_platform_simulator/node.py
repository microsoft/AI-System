# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Spec of nodes."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from enum import Enum
from device import *
import random


class Node(object):
    """Specification for nodes."""

    def __init__(self, name, gpus_count, gpus_spec = None):
        """
        Args:
            name: node name
            gpus_count: count
            gpus_spec: gpu spec
        """
        self._name = name
        self._gpus_count = gpus_count
        self._gpus = [] 
        # If define the GPU spec
        if gpus_spec == None:
            gpus_spec = ["K80", "P100", "P40", "A100_40GB", "V100_16GB"]
            for i in range(self._gpus_count):
                self._gpus.append(DEVICES[gpus_spec])
        else:
            for i in range(self._gpus_count):
                self._gpus.append(DEVICES[gpus_spec])   
        self._gpus_spec = gpus_spec
        self._free_gpus = self._gpus_count
        # random init per CPU request (is a multiple of the number of GPUs)
        cpu_count_size_set = {16,32,64,128,256}
        self._cpus = random.choice(tuple(cpu_count_size_set)) * self._gpus_count
        self._free_cpus = self._cpus
        host_mem_size_set_mb = {32 * 1024, 64 * 1024, 128 *1024, 256 *1024} # MB
        # random init task host memory request
        self._host_mems_mb = random.choice(tuple(host_mem_size_set_mb)) * self._gpus_count
        self._free_host_mems_mb = self._host_mems_mb

        self._allocated_jobs_dic = {} # job name -> task counts

    @property
    def name(self):
        return self._name

    @property
    def gpus_count(self):
        return self._gpus_count

    @property
    def free_gpus(self):
        return self._free_gpus

    @property
    def gpus_spec(self):
        return self._gpus_spec

    @property
    def cpus(self):
        return self._cpus

    @property
    def free_cpus(self):
        return self._free_cpus

    @property
    def host_mems_mb(self):
        return self._host_mems_mb

    @property
    def free_host_mems_mb(self):
        return self._free_host_mems_mb

    def contains_sufficient_resources(self, task_resouce_spec):
        (task_gpu, task_cpu, task_mem) = task_resouce_spec
        if self._free_gpus >= task_gpu and self._free_cpus > task_cpu and \
            self._free_host_mems_mb >= task_mem:
            return True
        else:
            return False 

    def allocate_task(self, job):
        if not contains_sufficient_resources(job.task_resouce_spec):
            return False

        (per_task_gpus, per_task_cpus, per_task_mems) = job.task_resource_spec
        self._free_gpus -= per_task_gpus
        self._free_cpus -= per_task_cpus
        self._free_host_mems_mb -= per_task_mems

        job_name = job.name
        if job_name in self._allocated_jobs_dic:
            self._allocated_jobs_dic[job_name] += 1
        else:
            self._allocated_jobs_dic[job_name] = 1
            
        job.allocate_one_task_to_node(self)
        return True 

    def release_task(self, job):
        (per_task_gpus, per_task_cpus, per_task_mems) = job.task_resource_spec
        self._free_gpus += per_task_gpus
        self._free_cpus += per_task_cpus
        self._free_host_mems_mb += per_task_mems  

        job_name = job.name
        if job_name in self._allocated_jobs_dic and \
            self._allocated_jobs_dic[job_name] > 1:
            self._allocated_jobs_dic[job_name] -= 1
        else:
            del self._allocated_jobs_dic[job_name] 
