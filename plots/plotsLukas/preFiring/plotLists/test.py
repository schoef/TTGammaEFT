#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
import sys
from math                             import pi
import copy
# RootTools
from RootTools.core.standard          import *

from TTGammaEFT.plots.multiplicity import multiplicity

plotListData    = []
plotListData   += multiplicity
plotListDataMC  = plotListData
