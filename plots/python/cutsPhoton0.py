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
cutsPhoton0 = []
    
cutsPhoton0.append( Plot(
    name      = 'photon0_hoe',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_hoe[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_hoe_tight',
    texX      = 'H/E(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_hoe[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 50, 0, 0.005 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_sieie',
    texX      = '#sigma_{i#etai#eta}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_sieie[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 50, 0.004, 0.012 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_pfRelIso03_chg[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_pfRelIso03_chg_tight',
    texX      = 'charged relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_pfRelIso03_chg[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_pfRelIso03_all[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 50, 0, 0.5 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_pfRelIso03_all_tight',
    texX      = 'relIso_{0.3}(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_pfRelIso03_all[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 50, 0, 0.05 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_electronVeto',
    texX      = 'eVeto(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_electronVeto[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

cutsPhoton0.append( Plot(
    name      = 'photon0_pixelSeed',
    texX      = 'hasPixelSeed(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_pixelSeed[0] if event.nPhoton > 0 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

#cutsPhoton0.append( Plot(
#    name      = 'photon0_cutBasedId',
#    texX      = 'cut-based ID(#gamma_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.Photon_cutBased[0] if event.nPhoton > 0 else defaultValue,
#    binning   = [ 4, 0, 4 ],
#))
