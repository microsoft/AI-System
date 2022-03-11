# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Spec of scheduler."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from algorithm import *
from event import *


class Scheduler(object):
    """Specification for schedulers."""

    def __init__(self, name, algorithm):
        """
        Args:
            name: node name
            algorithm: algorithm type
        """
        self._name = name
        self._algorithm = AlgorithmsFactory.build_algorithm(algo = algorithm)

    @property
    def name(self):
        return self._name

    def schedule_job(self, job, cluster):
        self._algorithm.schedule_job(job, cluster)
        return 

    def release_job(self, job, cluster):
        job.release_job(cluster)
        return
