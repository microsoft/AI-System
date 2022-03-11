# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Logger for debugging."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import sys

logger = logging.getLogger('root')
FORMAT = "[%(asctime)s;%(levelname)s;%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s "
logging.basicConfig(stream=sys.stdout, format=FORMAT)
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.INFO)
