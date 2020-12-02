#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Resetting Nest Kernel
nest.ResetKernel()

# Initializing Neurons, Brain connections and FrequencyDetectors
ctx_M1_layers = stim_all_model.main()

circuit = nest.Create('iaf_cond_alpha', 4)
