# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""Spec of clusters."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class Cluster(object):
    """Specification for cluster."""

    def __init__(self, name, nodes_count = None, nodes_spec = None):
        """
        Args:
            name: node name
            nodes_count: nodes count
            nodes_spec: node spec
        """
        self._name = name
        self._nodes_count = nodes_count
        self._nodes_spec = nodes_spec
        self._node_list = []

    @property
    def name(self):
        return self._name

    @property
    def nodes_count(self):
        return len(self._node_list)

    @property
    def nodes_list(self):
        return self._node_list

    @property
    def nodes_spec(self):
        return self._nodes_spec

    def add_node(self, node):
        self._node_list.append(node)
