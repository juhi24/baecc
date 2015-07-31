# -*- coding: utf-8 -*-
"""
@author: Jussi Tiira
"""
from snowfall import *
from read import *
import numpy as np
import matplotlib.pyplot as plt
from os import path

dtformat_default = '%d.%m. %H:%M'
dtformat_snex = '%Y %d %B %H UTC'

e = EventsCollection('cases/test.csv', dtformat_snex)
e.autoimport_data(autoshift=False, autobias=False, rule='6min', varinterval=True)

plt.close('all')
#plt.ioff()

for c in np.append(e.events.pluvio200.values, e.events.pluvio400.values):
    c.instr['pluvio'].shift_periods = -6
    c.instr['pluvio'].n_combined_intervals = 2

comb200 = e.events.pluvio200.sum()
comb400 = e.events.pluvio400.sum()
del(e) # may save memory
for comb in (comb200, comb400):
    axarr = comb.plot_vfits_in_density_ranges(separate=True, source_style='kde',
                                              fitargs={'force_flip': False},
                                              unfiltered=True, parallel=True)
    plt.axis((0.25,2,0.5,2.5))
    savepath = read.ensure_dir(path.join('../results/pip2015/vfits_density_ranges',
                                         comb.instr['pluvio'].name))
    plt.savefig(path.join(savepath, comb.dtstr('combined.eps')))