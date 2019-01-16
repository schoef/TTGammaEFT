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
cutsPhotonGood0 = []
    
cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_hoe',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_hoe if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_hoe_tight',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_hoe if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.005 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_sieie if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0.004, 0.012 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_chg if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_chg_tight',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_chg if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_all if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pfRelIso03_all_tight',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pfRelIso03_all if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_electronVeto',
    texX      = 'eVeto(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_electronVeto if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

cutsPhotonGood0.append( Plot(
    name      = 'photonGood0_pixelSeed',
    texX      = 'hasPixelSeed(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.PhotonGood0_pixelSeed if event.nPhotonGood > 0 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

#cutsPhotonGood0.append( Plot(
#    name      = 'photonGood0_cutBasedId',
#    texX      = 'cut-based ID(#gamma_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.PhotonGood0_cutBased if event.nPhotonGood > 0 else defaultValue,
#    binning   = [ 4, 0, 4 ],
#))
