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
jetClean0 = []
    
jetClean0.append( Plot(
    name      = 'cleanJet0_pt',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.JetClean_pt[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 20, 0, 600 ],
))

jetClean0.append( Plot(
    name      = 'cleanJet0_pt_tight',
    texX      = 'p_{T}(jet_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.JetClean_pt[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 20, 0, 200 ],
))

jetClean0.append( Plot(
    name      = 'cleanJet0_eta_tight',
    texX      = '#eta(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_eta[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 20, -3, 3 ],
))

jetClean0.append( Plot(
    name      = 'cleanJet0_eta',
    texX      = '#eta(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_eta[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 20, -5, 5 ],
))

jetClean0.append( Plot(
    name      = 'cleanJet0_absEta_tight',
    texX      = '|#eta|(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.JetClean_eta[0]) if event.nJetClean > 0 else defaultValue,
    binning   = [ 10, 0, 3 ],
))

jetClean0.append( Plot(
    name      = 'cleanJet0_absEta',
    texX      = '|#eta|(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.JetClean_eta[0]) if event.nJetClean > 0 else defaultValue,
    binning   = [ 10, 0, 5 ],
))

jetClean0.append( Plot(
    name      = 'cleanJet0_phi',
    texX      = '#phi(jet_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.JetClean_phi[0] if event.nJetClean > 0 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
