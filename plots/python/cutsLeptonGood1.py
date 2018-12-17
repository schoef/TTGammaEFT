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
cutsLeptonGood1 = []
    
cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_hoe',
    texX      = 'H/E(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_hoe[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==11 else defaultValue,
    binning   = [ 20, 0, 0.12 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_hoe_tight',
    texX      = 'H/E(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_hoe[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==11 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_eInvMinusPInv',
    texX      = '1/E - 1/p (l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_eInvMinusPInv[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==11 else defaultValue,
    binning   = [ 50, -0.05, 0.05 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_sip3d',
    texX      = 'sip3D(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_sip3d[1] if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 20, 0, 4.5 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_sieie',
    texX      = '#sigma_{i#etai#eta}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_sieie[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==11 else defaultValue,
    binning   = [ 20, 0, 0.02 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_pfRelIso03_chg',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_pfRelIso03_chg[1] if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 20, 0, 0.2 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_pfRelIso03_chg_tight',
    texX      = 'charged relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_pfRelIso03_chg[1] if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_pfRelIso03_all',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_pfRelIso03_all[1] if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 20, 0, 0.2 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_pfRelIso03_all_tight',
    texX      = 'relIso_{0.3}(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_pfRelIso03_all[1] if event.nLeptonGood > 1 else defaultValue,
    binning   = [ 20, 0, 0.05 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_convVeto',
    texX      = 'convVeto(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_convVeto[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==11 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_lostHits',
    texX      = 'lost hits(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_lostHits[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==11 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_cutBasedId',
    texX      = 'cut-based ID(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_cutBased[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==11 else defaultValue,
    binning   = [ 5, 0, 5 ],
))

cutsLeptonGood1.append( Plot(
    name      = 'leptonGood1_mediumID',
    texX      = 'medium ID(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.LeptonGood_mediumId[1] if event.nLeptonGood > 1 and abs(event.LeptonGood_pdgId[1])==13 else defaultValue,
    binning   = [ 2, 0, 2 ],
))

