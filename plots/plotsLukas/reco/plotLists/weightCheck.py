#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

from TTGammaEFT.plots.photonGood0      import photonGood0
from TTGammaEFT.plots.leptonGood0      import leptonGood0
from TTGammaEFT.plots.jetGood0         import jetGood0
from TTGammaEFT.plots.leptonGood1      import leptonGood1
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.beam             import beam

# plotList
plotListData  = []
plotListData += photonGood0 #for photon weight
plotListData += leptonGood0 #for lepton weight
plotListData += jetGood0
plotListData += multiplicityGood #for a lot
plotListData += beam #for PU weight

plotListDataMC = plotListData

