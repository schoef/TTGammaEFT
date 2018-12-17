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
from TTGammaEFT.plots.leptonGood1      import leptonGood1
from TTGammaEFT.plots.jetGood0         import jetGood0
from TTGammaEFT.plots.jetGood1         import jetGood1
from TTGammaEFT.plots.bjet0            import bjet0
from TTGammaEFT.plots.bjet1            import bjet1
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.mass             import mass
from TTGammaEFT.plots.met              import met
from TTGammaEFT.plots.beam             import beam
#from TTGammaEFT.plots.checks           import checks

# plotList
plotListData  = []
plotListData += photonGood0
plotListData += leptonGood0
plotListData += leptonGood1
plotListData += jetGood0
plotListData += jetGood1
plotListData += bjet0
plotListData += bjet1
plotListData += multiplicityGood
plotListData += mass
plotListData += met
plotListData += beam

plotListDataMC  = plotListData
#plotListDataMC += checks

