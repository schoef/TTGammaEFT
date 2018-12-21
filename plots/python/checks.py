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
checks = []
    
checks.append( Plot(
    name      = 'isTTG',
    texX      = 'Flag_{tt#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isTTGamma,
    binning   = [ 2, 0, 2 ],
))

checks.append( Plot(
    name      = 'isZG',
    texX      = 'Flag_{Z#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isZGamma,
    binning   = [ 2, 0, 2 ],
))

checks.append( Plot(
    name      = 'gamma0_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_photonCat[0] in event.nPhoton > 0 else defaultValue,
    binning   = [ 4, 0, 4 ],
))
