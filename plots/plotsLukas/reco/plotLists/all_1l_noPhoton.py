#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# TTGammaEFT
from TTGammaEFT.Tools.constants       import defaultValue

from TTGammaEFT.plots.leptonTight0              import leptonTight0
from TTGammaEFT.plots.leptonTight1              import leptonTight1
from TTGammaEFT.plots.jetGood0                  import jetGood0
from TTGammaEFT.plots.jetGood1                  import jetGood1
from TTGammaEFT.plots.bjetGood0                 import bjetGood0
from TTGammaEFT.plots.bjetGood1                 import bjetGood1
from TTGammaEFT.plots.multiplicityGoodNoPhoton  import multiplicityGoodNoPhoton
from TTGammaEFT.plots.massTight                 import massTight
from TTGammaEFT.plots.isolationTight            import isolationTight
from TTGammaEFT.plots.met                       import met
from TTGammaEFT.plots.ht                        import ht
from TTGammaEFT.plots.beam                      import beam

from TTGammaEFT.plots.cutsJetGood0        import cutsJetGood0
from TTGammaEFT.plots.cutsJetGood1        import cutsJetGood1
from TTGammaEFT.plots.cutsLeptonTight0    import cutsLeptonTight0
from TTGammaEFT.plots.cutsLeptonTight1    import cutsLeptonTight1

# plotList
plotListData  = []
plotListData += leptonTight0
plotListData += leptonTight1
plotListData += jetGood0
plotListData += jetGood1
plotListData += bjetGood0
plotListData += bjetGood1
plotListData += multiplicityGoodNoPhoton
plotListData += massTight
plotListData += isolationTight
plotListData += met
plotListData += ht
plotListData += beam

plotListData += cutsJetGood0
plotListData += cutsJetGood1
plotListData += cutsLeptonTight0
plotListData += cutsLeptonTight1

plotListDataMC = plotListData

