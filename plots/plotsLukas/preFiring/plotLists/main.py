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
from TTGammaEFT.plots.leptonGood0      import leptonGood0
from TTGammaEFT.plots.leptonGood1      import leptonGood1
from TTGammaEFT.plots.jet0         import jet0
from TTGammaEFT.plots.jet1         import jet1
from TTGammaEFT.plots.bjet0        import bjet0
from TTGammaEFT.plots.bjet1        import bjet1
from TTGammaEFT.plots.multiplicity import multiplicity
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.mass         import mass
from TTGammaEFT.plots.met          import met
from TTGammaEFT.plots.beam         import beam
#from TTGammaEFT.plots.checks       import checks

# plotList
plotListData  = []
plotListData += photon0
plotListData += leptonGood0
plotListData += leptonGood1
plotListData += jet0
plotListData += jet1
plotListData += bjet0
plotListData += bjet1
plotListData += multiplicity
plotListData += multiplicityGood
plotListData += mass
plotListData += met
plotListData += beam

plotListDataMC  = plotListData
#plotListDataMC += checks

