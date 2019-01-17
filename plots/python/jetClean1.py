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
jetClean1 = []
    
jetClean1.append( Plot(
    name      = 'cleanJet1_pt',
    texX      = 'p_{T}(jet_{1}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.JetClean_pt[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 20, 0, 600 ],
))

jetClean1.append( Plot(
    name      = 'cleanJet1_pt_tight',
    texX      = 'p_{T}(jet_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.JetClean_pt[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 20, 0, 200 ],
))

jetClean1.append( Plot(
    name      = 'cleanJet1_eta',
    texX      = '#eta(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_eta[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 20, -5, 5 ],
))

jetClean1.append( Plot(
    name      = 'cleanJet1_eta_tight',
    texX      = '#eta(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_eta[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 20, -3, 3 ],
))

jetClean1.append( Plot(
    name      = 'cleanJet1_absEta',
    texX      = '|#eta|(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.JetClean_eta[1]) if event.nJetClean > 1 else defaultValue,
    binning   = [ 10, 0, 5 ],
))

jetClean1.append( Plot(
    name      = 'cleanJet1_absEta_tight',
    texX      = '|#eta|(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.JetClean_eta[1]) if event.nJetClean > 1 else defaultValue,
    binning   = [ 10, 0, 3 ],
))

jetClean1.append( Plot(
    name      = 'cleanJet1_phi',
    texX      = '#phi(jet_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_phi[1] if event.nJetClean > 1 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
