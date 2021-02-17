# ---LICENSE-BEGIN - DO NOT CHANGE OR MOVE THIS HEADER
# This file is part of the Neurorobotics Platform software
# Copyright (C) 2014,2015,2016,2017 Human Brain Project
# https://www.humanbrainproject.eu
#
# The Human Brain Project is a European Commission funded project
# in the frame of the Horizon2020 FET Flagship plan.
# http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# ---LICENSE-END
"""
Support methods to load a brain network from a python file
"""

__author__ = "Lorenzo Vannucci, Sebastian Krach, Christopher Bignamini"

from hbp_nrp_cle.cle.CLEInterface import BrainTimeoutException

import imp
import logging


logger = logging.getLogger("BrainLoader")
__nest_brain_index = 0

# pylint: disable=global-statement
def load_py_network(path, nest_client):
    """
    Load a python network file

    :param path: path to the .py file
    """
    global __nest_brain_index # TODO: christopher investigate usage of __nest_brain_index global variable
    brain_module = imp.new_module('__brain_model' + str(__nest_brain_index))
#    brain_module = imp.load_source('__brain_model' + str(__nest_brain_index), path)
    populations = nest_client.load_network(path)
    for pop in populations:
        setattr(brain_module, pop, tuple(populations[pop]))
#    brain_module.circuit = tuple(populations['circuit'])
    __nest_brain_index += 1
    return brain_module
