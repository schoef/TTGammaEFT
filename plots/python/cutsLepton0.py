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
cutsLepton0 = []
    
cutsLepton0.append( Plot(
    name      = 'lepton0_hoe',
    texX      = 'H/E(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_hoe[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==11 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_hoe_tight',
    texX      = 'H/E(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_hoe[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==11 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_eInvMinusPInv[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==11 else defaultValue,
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_sip3d',
    texX      = 'sip3D(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_sip3d[0] if event.nLepton > 0 else defaultValue,
    binning   = [ 20, 0, 4.5 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_sieie[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==11 else defaultValue,
    binning   = [ 20, 0, 0.02 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_pfRelIso03_chg[0] if event.nLepton > 0 else defaultValue,
    binning   = [ 20, 0, 0.2 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_pfRelIso03_chg_tight',
    texX      = 'charged relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_pfRelIso03_chg[0] if event.nLepton > 0 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_pfRelIso03_all[0] if event.nLepton > 0 else defaultValue,
    binning   = [ 20, 0, 0.2 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_pfRelIso03_all_tight',
    texX      = 'relIso_{0.3}(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_pfRelIso03_all[0] if event.nLepton > 0 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_convVeto',
    texX      = 'convVeto(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_convVeto[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==11 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_lostHits',
    texX      = 'lost hits(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_lostHits[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==11 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_cutBasedId',
    texX      = 'cut-based ID(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_cutBased[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==11 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsLepton0.append( Plot(
    name      = 'lepton0_mediumID',
    texX      = 'medium ID(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_mediumId[0] if event.nLepton > 0 and abs(event.Lepton_pdgId[0])==13 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

