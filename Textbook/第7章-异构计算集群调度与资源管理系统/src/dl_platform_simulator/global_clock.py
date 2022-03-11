# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Global clock."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import datetime
from logger import logger

class GlobalClock(object):
    """Specification for events."""

    def __init__(self, first_event_timestamp):
        self._word_start_timestamp = first_event_timestamp
        self._current_timestamp = first_event_timestamp

    @property
    def word_start_timestamp(self):
        return self._word_start_timestamp

    @property
    def current_timestamp(self):
        return self._current_timestamp

    def set_timestamp(self, timestamp):
        assert timestamp >= self._current_timestamp
        self._current_timestamp = timestamp

