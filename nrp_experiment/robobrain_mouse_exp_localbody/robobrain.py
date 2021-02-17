#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Resetting Nest Kernel
nest.ResetKernel()

# Initializing Neurons, Brain connections and FrequencyDetectors
# ctx_M1_layers = stim_all_model.main()

### DUMMY BRAIN
M1_L1_ENGC = nest.Create('iaf_cond_alpha', 10)
M1_L1_ENGC = nest.Create('iaf_cond_alpha', 10)
M1_L1_SBC = nest.Create('iaf_cond_alpha', 10)
M1_L23_CC = nest.Create('iaf_cond_alpha', 10)
M1_L23_PV = nest.Create('iaf_cond_alpha', 10)
M1_L23_SST = nest.Create('iaf_cond_alpha', 10)
M1_L23_VIP = nest.Create('iaf_cond_alpha', 10)
M1_L5A_CC = nest.Create('iaf_cond_alpha', 10)
M1_L5A_CS = nest.Create('iaf_cond_alpha', 10)
M1_L5A_CT = nest.Create('iaf_cond_alpha', 10)
M1_L5A_PV = nest.Create('iaf_cond_alpha', 10)
M1_L5A_SST = nest.Create('iaf_cond_alpha', 10)
M1_L5B_CC = nest.Create('iaf_cond_alpha', 10)
M1_L5B_CS = nest.Create('iaf_cond_alpha', 10)
M1_L5B_PT = nest.Create('iaf_cond_alpha', 10)
M1_L5B_PV = nest.Create('iaf_cond_alpha', 10)
M1_L5B_SST = nest.Create('iaf_cond_alpha', 10)
M1_L6_CT = nest.Create('iaf_cond_alpha', 10)
M1_L6_PV = nest.Create('iaf_cond_alpha', 10)
M1_L6_SST = nest.Create('iaf_cond_alpha', 10)
                      

populations = {'M1_L1_ENGC': M1_L1_ENGC,
                  'M1_L1_SBC': M1_L1_SBC,
                  'M1_L23_CC': M1_L23_CC,
                  'M1_L23_PV': M1_L23_PV,
                  'M1_L23_SST': M1_L23_SST,
                  'M1_L23_VIP': M1_L23_VIP,
                  'M1_L5A_CC': M1_L5A_CC,
                  'M1_L5A_CS': M1_L5A_CS,
                  'M1_L5A_CT': M1_L5A_CT,
                  'M1_L5A_PV': M1_L5A_PV,
                  'M1_L5A_SST': M1_L5A_SST,
                  'M1_L5B_CC': M1_L5B_CC,
                  'M1_L5B_CS': M1_L5B_CS,
                  'M1_L5B_PT': M1_L5B_PT,
                  'M1_L5B_PV': M1_L5B_PV,
                  'M1_L5B_SST': M1_L5B_SST,
                  'M1_L6_CT': M1_L6_CT,
                  'M1_L6_PV': M1_L6_PV,
                  'M1_L6_SST': M1_L6_SST}
