#!/usr/bin/env python
''' Define list of plotList for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
plotList = []
    
plotList.append( Plot(
    name      = 'mllgamma',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mllgamma if event.nLepton >= 2 else -999,
    binning   = [ 35, 60, 200 ],
))

plotList.append( Plot(
    name      = 'gamma0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 6 GeV',
    attribute = lambda event, sample: event.Photon_pt[0] if event.nPhoton > 0 else -999,
    binning   = [ 19, 20, 115 ],
))

plotList.append( Plot(
    name      = 'gamma0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_eta[0] if event.nPhoton > 0 else -999,
    binning   = [ 20, -1.5, 1.5 ],
))

plotList.append( Plot(
    name      = 'gamma0_absEta',
    texX      = '|#eta|(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Photon_eta[0]) if event.nPhoton > 0 else -999,
    binning   = [ 9, 0, 1.5 ],
))

plotList.append( Plot(
    name      = 'nPhoton',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nPhoton,
    binning   = [ 3, 0, 3 ],
))

plotList.append( Plot(
    name      = 'nLepton',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nLepton,
    binning   = [ 3, 0, 3 ],
))

plotList.append( Plot(
    name      = 'nElectron',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nElectron,
    binning   = [ 3, 0, 3 ],
))

plotList.append( Plot(
    name      = 'nMuon',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nMuon,
    binning   = [ 3, 0, 3 ],
))

plotList.append( Plot(
    name      = 'nJet',
    texX      = 'N_{jet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nJet,
    binning   = [ 7, 0, 7 ],
))

plotList.append( Plot(
    name      = 'nBJet',
    texX      = 'N_{bJet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nBTag,
    binning   = [ 4, 0, 4 ],
))

