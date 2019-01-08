#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

# plotList
htGood = []
    
htGood.append( Plot(
    name      = 'htGood',
    texX      = 'H_{T} (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.htGood,
    binning   = [ 20, 0, 600 ],
))
