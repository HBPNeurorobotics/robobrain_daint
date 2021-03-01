#!/usr/bin/env python 

## This file was auto-generated by run.py called with the following arguments:
# run.py --whichSim stim_all_model --platform Local --nbcpu 8

## ID string of experiment:
# 2020_10_09_18_13_19_xp000000

## Reproducibility info:
#  platform = Local
#  git commit ID not available
#  Git status not available

simParams =\
{
    "channels": False,
    "channels_nb": 6,
    "channels_radius": 0.16,
    "circle_center": [],
    "dt": "0.1",
    "hex_radius": 0.24,
    "initial_ignore": 400.0,
    "macro_columns_nb": 7,
    "micro_columns_nb": 7,
    "msd": 123456,
    "nbcpu": 72,
    "nbnodes": 1,
    "overwrite_files": True,
    "scalefactor": [
        1.0,
        1.0
    ],
    "simDuration": 1000.0,
    "sim_model": {
        "BG_only": {
            "on": False,
            "regions": {
                "BG": True,
                "CB_M1": False,
                "CB_S1": False,
                "M1": False,
                "S1": False,
                "TH_M1": False,
                "TH_S1": False
            }
        },
        "CB_only": {
            "on": False,
            "regions": {
                "BG": False,
                "CB_M1": True,
                "CB_S1": True,
                "M1": False,
                "S1": False,
                "TH_M1": False,
                "TH_S1": False
            }
        },
        "M1_only": {
            "on": False,
            "regions": {
                "BG": False,
                "CB_M1": False,
                "CB_S1": False,
                "M1": True,
                "S1": False,
                "TH_M1": False,
                "TH_S1": False
            }
        },
        "S1_only": {
            "on": False,
            "regions": {
                "BG": False,
                "CB_M1": False,
                "CB_S1": False,
                "M1": False,
                "S1": True,
                "TH_M1": False,
                "TH_S1": False
            }
        },
        "TH_only": {
            "on": False,
            "regions": {
                "BG": False,
                "CB_M1": False,
                "CB_S1": False,
                "M1": False,
                "S1": False,
                "TH_M1": True,
                "TH_S1": True
            }
        },
        "arm_movement": {
            "on": False,
            "regions": {
                "BG": True,
                "CB_M1": False,
                "CB_S1": False,
                "M1": True,
                "S1": True,
                "TH_M1": True,
                "TH_S1": True
            }
        },
        "cb_learning": {
            "delta_t": 500.0,
            "on": False,
            "regions": {
                "BG": True,
                "CB_M1": True,
                "CB_S1": True,
                "M1": True,
                "S1": True,
                "TH_M1": True,
                "TH_S1": True
            },
            "trials_nb": 1
        },
        "multiple_arm_reaching": {
            "delta_t": 500.0,
            "on": False,
            "regions": {
                "BG": True,
                "CB_M1": True,
                "CB_S1": True,
                "M1": True,
                "S1": True,
                "TH_M1": True,
                "TH_S1": True
            },
            "trials_nb": 3
        },
        "reinf_learning": {
            "delta_t": 500.0,
            "on": False,
            "regions": {
                "BG": True,
                "CB_M1": False,
                "CB_S1": False,
                "M1": True,
                "S1": True,
                "TH_M1": True,
                "TH_S1": True
            },
            "trials_nb": 5
        },
        "resting_state": {
            "on": True,
            "regions": {
                "BG": False,
                "CB_M1": False,
                "CB_S1": False,
                "M1": True,
                "S1": False,
                "TH_M1": False,
                "TH_S1": False
            }
        },
        "single_arm_reaching": {
            "on": False,
            "regions": {
                "BG": True,
                "CB_M1": True,
                "CB_S1": True,
                "M1": True,
                "S1": True,
                "TH_M1": True,
                "TH_S1": True
            }
        }
    },
    "whichSim": "stim_all_model"
}