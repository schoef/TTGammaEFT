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
bjet1 = []
    
bjet1.append( Plot(
    name      = 'bjet1_pt',
    texX      = 'p_{T}(b_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Bj1_pt if event.nBTag > 1 else defaultValue,
    binning   = [ 20, 0, 200 ],
))

bjet1.append( Plot(
    name      = 'bjet1_eta',
    texX      = '#eta(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj1_eta if event.nBTag > 1 else defaultValue,
    binning   = [ 20, -5, 5 ],
))

bjet1.append( Plot(
    name      = 'bjet1_absEta',
    texX      = '|#eta|(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Bj1_eta) if event.nBTag > 1 else defaultValue,
    binning   = [ 10, 0, 5 ],
))

bjet1.append( Plot(
    name      = 'bjet1_phi',
    texX      = '#phi(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj1_phi if event.nBTag > 1 else defaultValue,
    binning   = [ 10, -pi, pi ],
))
