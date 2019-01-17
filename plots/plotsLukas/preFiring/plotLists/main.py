#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                              import pi

# RootTools
from RootTools.core.standard           import *

# TTGammaEFT
from TTGammaEFT.Tools.constants        import defaultValue

from TTGammaEFT.plots.leptonGood0      import leptonGood0
from TTGammaEFT.plots.leptonGood1      import leptonGood1
from TTGammaEFT.plots.lepton0          import lepton0
from TTGammaEFT.plots.lepton1          import lepton1
from TTGammaEFT.plots.jet0             import jet0
from TTGammaEFT.plots.jet1             import jet1
from TTGammaEFT.plots.jetClean0        import jetClean0
from TTGammaEFT.plots.jetClean1        import jetClean1
from TTGammaEFT.plots.multiplicity     import multiplicity
from TTGammaEFT.plots.multiplicityGood import multiplicityGood
from TTGammaEFT.plots.met              import met
from TTGammaEFT.plots.ht               import ht
from TTGammaEFT.plots.beam             import beam
from TTGammaEFT.plots.metSig           import metSig

# plotList
plotListData  = []
plotListData += leptonGood0
plotListData += leptonGood1
plotListData += lepton0
plotListData += lepton1
plotListData += jet0
plotListData += jet1
plotListData += jetClean0
plotListData += jetClean1
plotListData += multiplicity
plotListData += multiplicityGood
plotListData += met
plotListData += ht
plotListData += beam
plotListData += metSig

plotListDataMC  = plotListData

