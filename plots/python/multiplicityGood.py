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
multiplicityGood = []
    
multiplicityGood.append( Plot(
    name      = 'nPhotonGood',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nPhotonGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nLeptonGood',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nLeptonGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nElectronGood',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nElectronGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nMuonGood',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nMuonGood,
    binning   = [ 4, 0, 4 ],
))

multiplicityGood.append( Plot(
    name      = 'nJetGood',
    texX      = 'N_{jet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nJetGood,
    binning   = [ 10, 0, 10 ],
))

multiplicityGood.append( Plot(
    name      = 'nBJetGood',
    texX      = 'N_{bJet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nBTag,
    binning   = [ 4, 0, 4 ],
))

