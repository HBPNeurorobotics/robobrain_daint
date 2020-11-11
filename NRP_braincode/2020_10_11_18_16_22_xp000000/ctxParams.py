#!/usr/bin/env python 

## This file was auto-generated by run.py called with the following arguments:
# run.py --whichSim stim_all_model --platform Local --nbcpu 8

## ID string of experiment:
# 2020_10_09_18_13_19_xp000000

## Reproducibility info:
#  platform = Local
#  git commit ID not available
#  Git status not available

ctxParams =\
{
    "S1": {
        "connection_info": {
            "internal": "S1_internal_connection.pickle"
        },
        "neuro_info": {
            "L1": {
                "ENGC": {
                    "Cellcount_mm2": 1555.61356,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "SBC": {
                    "Cellcount_mm2": 3019.72044,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                }
            },
            "L2": {
                "PV": {
                    "Cellcount_mm2": 160.5344711,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "Pyr": {
                    "Cellcount_mm2": 2714.12822,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "E",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "SST": {
                    "Cellcount_mm2": 64.19044042,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "VIP": {
                    "Cellcount_mm2": 331.1808684,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                }
            },
            "L3": {
                "PV": {
                    "Cellcount_mm2": 433.8706005,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "Pyr": {
                    "Cellcount_mm2": 15191.19693,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "E",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "SST": {
                    "Cellcount_mm2": 173.4851383,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "VIP": {
                    "Cellcount_mm2": 895.0703312,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                }
            },
            "L4": {
                "PV": {
                    "Cellcount_mm2": 1364.873436,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "Pyr": {
                    "Cellcount_mm2": 19545.61641,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "E",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "SST": {
                    "Cellcount_mm2": 357.863157,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                }
            },
            "L5A": {
                "PV": {
                    "Cellcount_mm2": 710.7989056,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "Pyr": {
                    "Cellcount_mm2": 4510.488672,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "E",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "SST": {
                    "Cellcount_mm2": 409.7844224,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                }
            },
            "L5B": {
                "PV": {
                    "Cellcount_mm2": 1301.725431,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "Pyr": {
                    "Cellcount_mm2": 12489.12546,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "E",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "SST": {
                    "Cellcount_mm2": 1112.640111,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                }
            },
            "L6": {
                "PV": {
                    "Cellcount_mm2": 1533.281691,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 10.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "Pyr": {
                    "Cellcount_mm2": 25072.14168,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "E",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                },
                "SST": {
                    "Cellcount_mm2": 1129.246629,
                    "E_ex": 0.0,
                    "E_in": -80.0,
                    "E_rest": -70.0,
                    "EorI": "I",
                    "I_ex": 0.0,
                    "absolute_refractory_period": 1.0,
                    "membrane_time_constant": 20.0,
                    "neuron_model": "iaf_cond_alpha",
                    "reset_value": -70.0,
                    "spike_threshold": -50.0,
                    "tau_syn_ex": 0.5,
                    "tau_syn_in": 3.33
                }
            }
        },
        "structure_info": {
            "Layer_Cellcount_mm2": [
                4575.334,
                3270.034,
                16693.623,
                21268.353,
                5631.072,
                14903.491,
                27734.67
            ],
            "Layer_Name": [
                "L1",
                "L2",
                "L3",
                "L4",
                "L5A",
                "L5B",
                "L6"
            ],
            "layer_depth": [
                0,
                0.128,
                0.184,
                0.419,
                0.626,
                0.733,
                1.006,
                1.366
            ],
            "layer_thickness": [
                0.128,
                0.056,
                0.235,
                0.207,
                0.107,
                0.273,
                0.36
            ],
            "region_name": "S1",
            "region_size": [
                1.0,
                1.0,
                1.366
            ]
        }
    }
}