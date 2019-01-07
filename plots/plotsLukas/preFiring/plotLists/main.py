#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                              import pi

# RootTools
from RootTools.core.standard           import *

# TTGammaEFT
from TTGammaEFT.Tools.constants        import defaultValue

from TTGammaEFT.plots.photon0          import photon0
from TTGammaEFT.plots.leptonGood0      import leptonGood0
from TTGammaEFT.plots.leptonGood1      import leptonGood1
from TTGammaEFT.plots.lepton0          import lepton0
from TTGammaEFT.plots.lepton1          import lepton1
from TTGammaEFT.plots.jetGood0         import jetGood0
from TTGammaEFT.plots.jetGood1         import jetGood1
from TTGammaEFT.plots.jet0             import jet0
from TTGammaEFT.plots.jet1             import jet1
from TTGammaEFT.plots.bjetGood0        import bjetGood0
from TTGammaEFT.plots.bjetGood1        import bjetGood1
from TTGammaEFT.plots.multiplicity     import multiplicity
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.massGood         import massGood
from TTGammaEFT.plots.met              import met
from TTGammaEFT.plots.beam             import beam
from TTGammaEFT.plots.metSig           import metSig
from TTGammaEFT.plots.metSigGood       import metSigGood
#from TTGammaEFT.plots.checks           import checks

# plotList
plotListData  = []
plotListData += photon0
plotListData += lepton0
plotListData += lepton1
plotListData += leptonGood0
plotListData += leptonGood1
plotListData += jet0
plotListData += jet1
plotListData += jetGood0
plotListData += jetGood1
plotListData += bjetGood0
plotListData += bjetGood1
plotListData += multiplicity
plotListData += multiplicityGood
plotListData += massGood
plotListData += met
plotListData += beam
plotListData += metSig
plotListData += metSigGood

plotListDataMC  = plotListData
#plotListDataMC += checks

