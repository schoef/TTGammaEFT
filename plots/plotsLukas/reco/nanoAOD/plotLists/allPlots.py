#!/usr/bin/env python
''' Define list of plots for plot script
'''

# RootTools
from RootTools.core.standard          import *

# Plots
plots = []
    
plots.append( Plot(
    name      = 'Photon_pT',
    texX      = 'p_{T}(#gamma) (GeV)',
    texY      = 'Number of Events / 20 GeV',
    attribute = lambda event, sample: event.Photon_pt[0],
    binning   = [ 20, 0, 400 ],
))

