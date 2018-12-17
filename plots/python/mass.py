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
mass = []
    
mass.append( Plot(
    name      = 'mL0Gamma',
    texX      = 'M(#gamma,l_{0}) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mL0Gamma if event.nLepton >= 1 and event.nPhoton >= 1 else defaultValue,
    binning   = [ 50, 0, 200 ],
))

mass.append( Plot(
    name      = 'mL1Gamma',
    texX      = 'M(#gamma,l_{1}) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mL1Gamma if event.nLepton >= 2 and event.nPhoton >= 1 else defaultValue,
    binning   = [ 50, 0, 200 ],
))

mass.append( Plot(
    name      = 'mll',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mll if event.nLepton >= 2 else defaultValue,
    binning   = [ 50, 0, 200 ],
))

mass.append( Plot(
    name      = 'mllgamma',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mllgamma if event.nLepton >= 2 else defaultValue,
    binning   = [ 50, 0, 200 ],
))

mass.append( Plot(
    name      = 'm3',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.m3 if event.nJet >= 3 else defaultValue,
    binning   = [ 50, 0, 250 ],
))

mass.append( Plot(
    name      = 'm3wBJet',
    texX      = 'M_{3} w/ 1 BJet (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.m3wBJet if event.nJet >= 3 and event.nBTag >= 1 else defaultValue,
    binning   = [ 50, 0, 250 ],
))
