#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Resetting Nest Kernel
nest.ResetKernel()

# Initializing Neurons, Brain connections and FrequencyDetectors
ctx_M1_layers = stim_all_model.main()


a = 3.0

b = 3.2


circuit = ctx_M1_layers # nest.Create('iaf_cond_alpha', 4)

