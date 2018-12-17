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
isolation = []

# Lepton Photon    
isolation.append( Plot(
    name      = 'dRL0Gamma0',
    texX      = '#DeltaR(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.l0GammadR if event.nPhoton >= 1 and event.nLepton >= 1 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'dPhiL0Gamma0',
    texX      = '#Delta#phi(#gamma_{0},l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.l0GammadPhi if event.nPhoton >= 1 and event.nLepton >= 1 else defaultValue,
    binning   = [ 40, 0, pi ],
))

isolation.append( Plot(
    name      = 'dRL1Gamma0',
    texX      = '#DeltaR(#gamma_{0},l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.l1GammadR if event.nPhoton >= 1 and event.nLepton >= 2 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'dPhiL1Gamma0',
    texX      = '#Delta#phi(#gamma_{0},l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.l1GammadPhi if event.nPhoton >= 1 and event.nLepton >= 2 else defaultValue,
    binning   = [ 40, 0, pi ],
))

# Jet Photon    
isolation.append( Plot(
    name      = 'dRJ0Gamma0',
    texX      = '#DeltaR(#gamma_{0},j_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.j0GammadR if event.nPhoton >= 1 and event.nJet >= 1 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'dPhiJ0Gamma0',
    texX      = '#Delta#phi(#gamma_{0},j_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.j0GammadPhi if event.nPhoton >= 1 and event.nJet >= 1 else defaultValue,
    binning   = [ 40, 0, pi ],
))

isolation.append( Plot(
    name      = 'dRJ1Gamma0',
    texX      = '#DeltaR(#gamma_{0},j_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.j1GammadR if event.nPhoton >= 1 and event.nJet >= 2 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'dPhiJ1Gamma0',
    texX      = '#Delta#phi(#gamma_{0},j_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.j1GammadPhi if event.nPhoton >= 1 and event.nJet >= 2 else defaultValue,
    binning   = [ 40, 0, pi ],
))

# Min dR (for cuts)
isolation.append( Plot(
    name      = 'mindRJetGamma',
    texX      = 'min(#DeltaR(#gamma, jet))',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.photonJetdR if event.nJet >= 1 and event.nPhoton >= 1 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'mindRJetLepton',
    texX      = 'min(#DeltaR(lep, jet))',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.leptonJetdR if event.nJet >= 1 and event.nLepton >= 1 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'mindRLepGamma',
    texX      = 'min(#DeltaR(#gamma, l))',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.photonLepdR if event.nLepton >= 1 and event.nPhoton >= 1 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

# ll
isolation.append( Plot(
    name      = 'dRll',
    texX      = '#DeltaR(ll)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.lldR if event.nLepton >= 2 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'dPhill',
    texX      = '#Delta#phi(ll)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.lldPhi if event.nLepton >= 2 else defaultValue,
    binning   = [ 40, 0, pi ],
))

# bb
isolation.append( Plot(
    name      = 'dRbb',
    texX      = '#DeltaR(bb)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.bbdR if event.nBTag >= 2 else defaultValue,
    binning   = [ 40, 0, 4 ],
))

isolation.append( Plot(
    name      = 'dPhibb',
    texX      = '#Delta#phi(bb)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.bbdPhi if event.nBTag >= 2 else defaultValue,
    binning   = [ 40, 0, pi ],
))
