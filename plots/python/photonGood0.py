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
photonGood0 = []
    
photonGood0.append( Plot(
    name      = 'photonGood0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.PhotonGood_pt[0] if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 19, 20, 115 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood_eta[0] if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 24, -1.8, 1.8 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_absEta',
    texX      = '|#eta|(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.PhotonGood_eta[0]) if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 9, 0, 1.5 ],
))

photonGood0.append( Plot(
    name      = 'photonGood0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood_phi[0] if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
