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
metSigGood = []

metSigGood.append( Plot(
    name      = 'MetSigGood',
    texX      = 'E_{T}^{miss}/#sqrt{H_{T}} (GeV^{1/2})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString('METSigGood/F'),
    binning   = [80,20,100],
))

metSigGood.append( Plot(
    name      = 'MetSigGood_tight',
    texX      = 'E_{T}^{miss}/#sqrt{H_{T}} (GeV^{1/2})',
    texY      = 'Number of Events',
    attribute = TreeVariable.fromString('METSigGood/F'),
    binning   = [30,0,30],
))
