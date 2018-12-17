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
leptonGood0 = []

leptonGood0.append( Plot(
    name      = 'leptonGood0_pt',
    texX      = 'p_{T}(l_{0}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.LeptonGood_pt[0] if event.nLeptonGood > 0 else defaultValue,
    binning   = [ 20, 0, 300 ],
))

leptonGood0.append( Plot(
    name      = 'leptonGood0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_eta[0] if event.nLeptonGood > 0 else defaultValue,
    binning   = [ 30, -3, 3 ],
))

leptonGood0.append( Plot(
    name      = 'leptonGood0_absEta',
    texX      = '|#eta|(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.LeptonGood_eta[0]) if event.nLeptonGood > 0 else defaultValue,
    binning   = [ 15, 0, 3 ],
))

leptonGood0.append( Plot(
    name      = 'leptonGood0_phi',
    texX      = '#phi(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_phi[0] if event.nLeptonGood > 0 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
