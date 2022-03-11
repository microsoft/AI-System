# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Copyright 2018 The paleo Team

This file is adapted from https://github.com/TalwalkarLab/paleo
"""

"""Spec of devices."""

from enum import Enum


class GPUState(Enum):
    FREE = 1
    ALLOCATED = 2
    BAD = 3

class Device(object):
    """Specification for devices."""

    def __init__(self, name, clock, peek_gflop, mem_bandwidth, mem_size = 0, \
        is_gpu=False):
        """
        Args:
            name: device name
            clock: MHz
            peek_gflop: GFLOPS
            mem_bandwidth: GB/sec
        """
        self._name = name
        self.clock = clock
        self.peek_gflop = float(peek_gflop)  # single precision
        self.mem_bandwidth = float(mem_bandwidth)
        self.mem_size = float(mem_size)
        self._is_gpu = is_gpu
        self._state = GPUState.FREE
        self._jobid = None

    @property
    def name(self):
        return self._name

    @property
    def is_gpu(self):
        return self._is_gpu

    @property
    def state(self):
        return self._state

    def set_device_state(self, state):
        self._state = state

    @property
    def allocated_jobid(self):
        return self._jobid

    def allocate_jobid(self, jobid):
        self._jobid = jobid

_Gbps = 1
_GBps = 8


class Network(object):
    def __init__(self, name, bandwidth):
        """
        Args:
            name: name of this network connection.
            bandwidth: in Gbps.
        """
        self._name = name
        self._bandwidth_Gbps = bandwidth

    @property
    def name(self):
        return self._name

    @property
    def bandwidth(self):
        return self._bandwidth_Gbps


AWS = Network('AWS', bandwidth=2 * _Gbps)
ETHERNET = Network('Ethernet', bandwidth=10 * _Gbps)
ETHERNET_20 = Network('Ethernet', bandwidth=20 * _Gbps)
INFINIBAND = Network('Infiniband', bandwidth=70 * _Gbps)
PCIe_2 = Network('PCIe 2.0', bandwidth=8 * _GBps)  # One weird trick: 6 GB/s
PCIe_3 = Network('PCIe 3.0', bandwidth=16 * _GBps)

# Here we assume PCIe x16.
# PCIe 1.0: 150MB/s per lane per direction.
# PCIe 2.0: 500MB/s per lane per direction.
# PCIe 3.0: 1GB/s per lane per direction.

NETWORKS = {
    'aws': AWS,
    'ethernet': ETHERNET,
    'ethernet20': ETHERNET_20,
    'infiniband': INFINIBAND,
    'pcie2': PCIe_2,
    'pcie3': PCIe_3
}

# Predefined devices.
GPU_TITAN_X = Device('Titan X',
                     clock=1000,
                     peek_gflop=6144,
                     mem_bandwidth=336.5,
                     is_gpu=True)

GPU_K20 = Device('K20',
                 clock=1000,
                 peek_gflop=3520,
                 mem_bandwidth=208,
                 is_gpu=True)

GPU_K20X = Device('K20X',
                  clock=1000,
                  peek_gflop=3935,
                  mem_bandwidth=250,
                  is_gpu=True)

GPU_K40 = Device('K40',
                 clock=745,
                 peek_gflop=4290,
                 mem_bandwidth=288,
                 is_gpu=True)

#ref: https://www.techpowerup.com/gpu-specs/tesla-k80.c2616
GPU_K80 = Device(
    'K80', clock=560, peek_gflop=5600, mem_bandwidth=480, mem_size=24, \
        is_gpu=True)
#ref: https://en.wikipedia.org/wiki/Nvidia_Tesla
Azure_GPU_K80 = Device(
    'K80_Azure', clock=560, peek_gflop=5600/2, mem_bandwidth=(480 / 2), \
    mem_size=(24 / 2), is_gpu=True)

GPU_P100 = Device(
    'P100', clock=1190, peek_gflop=9519, mem_bandwidth=720, mem_size=16, \
    is_gpu=True)

#https://www.nvidia.com/en-us/deep-learning-ai/solutions/inference-platform/hpc/
GPU_P40 = Device(
    'P40', clock=1300, peek_gflop=10007, mem_bandwidth=480, mem_size=22.3, \
    is_gpu=True)

GPU_V100_16GB = Device(
    'V100_16GB', clock=1246, peek_gflop=14028, mem_bandwidth=980, mem_size=16, \
    is_gpu=True)

#https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-32-gb.c3185
GPU_V100_32GB = Device(
    'V100_32GB', clock=1290, peek_gflop=14028, mem_bandwidth=980, mem_size=32, \
     is_gpu=True)

GPU_GEFORCE_780_TI = Device('GeForce 780 Ti',
                            clock=875,
                            peek_gflop=5040,
                            mem_bandwidth=336,
                            is_gpu=True)

GPU_GEFORCE_750M = Device('GeForce 750 M',
                          clock=941,
                          peek_gflop=722.7,
                          mem_bandwidth=80,
                          is_gpu=True)

CPU_I7_5930K = Device('CPU i7 5930K',
                      clock=6 * 35000,
                      peek_gflop=289,
                      mem_bandwidth=68)

# https://en.wikipedia.org/wiki/Tensor_processing_unit
# https://www.tomshardware.com/news/tpu-v2-google-machine-learning,35370.html
TPU_V1 = Device(
    'TPU_V1', clock=700, peek_gflop=45 * 1024, mem_bandwidth= 34 * 4, mem_size= 8 * 4, \
     is_gpu=False) # four chip modules, not clock use v1 HZ as no info provided

TPU_V2 = Device(
    'TPU_V2', clock=700, peek_gflop=180 * 1024, mem_bandwidth= 600 * 4, mem_size= 64, \
     is_gpu=False) # four chip modules, not clock use v1 HZ as no info provided

TPU_V3 = Device(
    'TPU_V3', clock=700, peek_gflop=420 * 1024, mem_bandwidth=4800, mem_size=128, \
     is_gpu=False) # mem band extend v2 TPU and cloud use v1 clock

GPU_A100_40GB = Device(
    'A100_40GB', clock=1246, peek_gflop=19500, mem_bandwidth=1555, mem_size=40, \
    is_gpu=True)

GPU_A100_80GB = Device(
    'A100_80GB', clock=1246, peek_gflop=19500, mem_bandwidth=2021, mem_size=80, \
    is_gpu=True)

DEVICES = {
    'A100_40GB': GPU_A100_40GB,
    'A100_80GB': GPU_A100_80GB,
    'TITAN_X': GPU_TITAN_X,
    'K20': GPU_K20,
    'K20X': GPU_K20X,
    'K40': GPU_K40,
    'K80': GPU_K80,
    'GEFORCE_780_TI': GPU_GEFORCE_780_TI,
    'GEFORCE_750_M': GPU_GEFORCE_750M,
    'CPU_I7': CPU_I7_5930K,
    'K80_Azure': Azure_GPU_K80,
    'P100': GPU_P100,
    'P40': GPU_P40,
    'V100_16GB': GPU_V100_16GB,
    'V100_32GB': GPU_V100_32GB,
    'TPU_V1': TPU_V1,
    'TPU_V2': TPU_V2,
    'TPU_V3': TPU_V3
}
