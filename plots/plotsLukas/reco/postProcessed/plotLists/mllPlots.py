#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
plotList = []
    
plotList.append( Plot(
    name      = 'mll',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mll if event.nLepton >= 2 else -999,
    binning   = [ 50, 0, 200 ],
))

plotList.append( Plot(
    name      = 'mllgamma',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mllgamma if event.nLepton >= 2 else -999,
    binning   = [ 50, 0, 200 ],
))

