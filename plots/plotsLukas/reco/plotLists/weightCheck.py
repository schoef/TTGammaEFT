#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

from TTGammaEFT.plots.photon0      import photon0
from TTGammaEFT.plots.lepton0      import lepton0
from TTGammaEFT.plots.jet0      import jet0
from TTGammaEFT.plots.lepton1      import lepton1
from TTGammaEFT.plots.multiplicity import multiplicity
from TTGammaEFT.plots.beam         import beam

# plotList
plotListData  = []
plotListData += photon0 #for photon weight
plotListData += lepton0 #for lepton weight
plotListData += jet0
plotListData += multiplicity #for a lot
plotListData += beam #for PU weight

plotListDataMC = plotListData

