# -*- coding: utf-8 -*-
"""
@author: Jussi Tiira
"""
import gc
scriptnames = ['scr_case_overview.py', 'scr_histograms.py', 'scr_psd_plots.py',
               'scr_d0-rho_combined.py', 'scr_vfits_density_ranges_combined.py']
for scriptname in scriptnames:
    runfile(scriptname)
    gc.collect()