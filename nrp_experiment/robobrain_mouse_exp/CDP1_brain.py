# -*- coding: utf-8 -*-
"""
This file contains the setup of the neuronal network running the Husky experiment with neuronal image recognition
"""
# pragma: no cover

__author__ = 'Lazar Mateev, Georg Hinkel'

import hbp_nrp_cle.tf_framework as nrp
import logging
from hbp_nrp_cle.brainsim import simulator as sim
import numpy as np
import h5py

logger = logging.getLogger(__name__)


def create_brain():
    """
    Initializes PyNN with the neuronal network that has to be simulated
    """
    import os

    h5_file_path = os.path.join(os.environ.get('NRP_MODELS_DIRECTORY'), 'brain_model/CDP1_brain_model_700_neurons.h5')
    h5file = h5py.File(h5_file_path, "r")

    #sim.setup(timestep=0.1, min_delay=0.1, max_delay=20.0, threads=1, debug=True)

    N = (h5file["x"].value).shape[0]

    cells = sim.Population(N, sim.IF_cond_alpha, {})

    for i, gid_ in enumerate(range(1, N + 1)):
        hasSyns = True
        try:
            r_syns = h5file["syn_" + str(gid_)].value
            r_synsT = h5file["synT_" + str(gid_)].value
        except:
            hasSyns = False
        if hasSyns and i < 10:
            params = {'U': 1.0, 'tau_rec': 0.0, 'tau_facil': 0.0}; syndynamics = sim.SynapseDynamics(
                fast=sim.TsodyksMarkramMechanism(**params))
            sim.Projection(cells[i:i + 1], cells[r_synsT - 1], sim.FixedNumberPostConnector(
                n=r_synsT.shape[0]), synapse_dynamics=syndynamics)

    population = cells
    h5file.close()

    logger.info("Circuit description: " + str(population.describe()))
    return population

circuit = create_brain()
