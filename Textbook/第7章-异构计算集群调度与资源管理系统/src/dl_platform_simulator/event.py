# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Spec of event."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import datetime
from logger import logger


class EventsFactory(object):
    """ simple factory for events
    """
    @staticmethod
    def build_event(event):
        events = {
           "submit_job": SubmitJobEvent,
           "release_job": ReleaseJobEvent,
           "profile_cluster": ProfileClusterEvent
        }
        return events[event]

class Event(object):
    """Specification for events."""

    def __init__(self, name, timestamp = None):
        """
        Args:
            name: node name
        """
        self._name = name
        self._type = "base"
        self._timestamp = timestamp

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def timestamp(self):
        return self._timestamp

class SubmitJobEvent(Event):
    """Specification for job submit events."""

    def __init__(self, job):
        """
        Args:
            name: node name
        """
        name = "submit_job_{}".format(job.jobid)
        super(SubmitJobEvent, self).__init__(name)
        self._name = name
        self._type = "submit_job"
        self._timestamp = datetime.timestamp(job.submitted_time)
        self._job = job

    @property
    def job(self):
        return self._job


class ReleaseJobEvent(Event):
    """Specification for release events."""

    def __init__(self, job, released_time):
        """
        Args:
            name: node name
        """
        name = "release_job_{}".format(job.jobid)
        super(ReleaseJobEvent, self).__init__(name)
        self._name = name
        self._type = "release_job"
        self._timestamp = datetime.timestamp(released_time)
        self._job = job

    @property
    def job(self):
        return self._job

class ProfileClusterEvent(Event):
    """Specification for logging cluster metrics events."""

    def __init__(self, name, timestamp):
        """
        Args:
            name: node name
        """
        super(ProfileClusterEvent, self).__init__(name)
        self._name = name
        self._type = "profile_cluster"
        self._timestamp = timestamp
