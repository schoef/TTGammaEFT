#!/usr/bin/env python
''' Define list of plots for plot script for comparison with StopsDilepton
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
plotList = []


plotList.append(Plot(
    name = 'PV_npvs', texX = 'N_{PV} (total)', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "PV_npvs/I" ),
    binning=[50,0,50],
))

plotList.append(Plot(
      texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
      attribute = TreeVariable.fromString( "MET_pt/F" ),
      binning=[400/20,0,400],
))
    
plotList.append(Plot(
      texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
      attribute = TreeVariable.fromString( "MET_phi/F" ),
      binning=[10,-pi,pi],
))

plotList.append(Plot(
    texX = 'number of jets', texY = 'Number of Events',
    attribute = TreeVariable.fromString('nJet/I'),
    binning=[14,0,14],
))

plotList.append(Plot(
    texX = 'number of medium b-tags (CSVM)', texY = 'Number of Events',
    attribute = TreeVariable.fromString('nBTag/I'),
    binning=[8,0,8],
))

plotList.append(Plot(
    texX = 'm(ll) of leading dilepton (GeV)', texY = 'Number of Events / 4 GeV',
    attribute = TreeVariable.fromString( "mll/F" ),
    binning=[200/4,0,200],
))

plotList.append( Plot(
    name      = 'l0_pt',
    texX      = 'p_{T}(l_{0}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.Lepton_pt[0] if event.nLepton > 0 else -999,
    binning   = [ 20, 0, 300 ],
))

plotList.append( Plot(
    name      = 'l0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Lepton_eta[0]) if event.nLepton > 0 else -999,
    binning   = [ 15, 0, 3 ],
))

plotList.append( Plot(
    name      = 'l0_phi',
    texX      = '#phi(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_phi[0] if event.nLepton > 0 else -999,
    binning   = [ 10, -pi, pi ],
))

plotList.append( Plot(
    name      = 'l1_pt',
    texX      = 'p_{T}(l_{1}) (GeV)',
    texY      = 'Number of Events / 15 GeV',
    attribute = lambda event, sample: event.Lepton_pt[1] if event.nLepton > 1 else -999,
    binning   = [ 20, 0, 300 ],
))

plotList.append( Plot(
    name      = 'l1_eta',
    texX      = '#eta(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Lepton_eta[1]) if event.nLepton > 1 else -999,
    binning   = [ 15, 0, 3 ],
))

plotList.append( Plot(
    name      = 'l1_phi',
    texX      = '#phi(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_phi[1] if event.nLepton > 1 else -999,
    binning   = [ 10, -pi, pi ],
))

plotList.append( Plot(
    name      = 'j0_pt',
    texX      = 'p_{T}(j_{0}) (GeV)',
    texY      = 'Number of Events / 30 GeV',
    attribute = lambda event, sample: event.Jet_pt[0] if event.nJet > 0 else -999,
    binning   = [ 20, 0, 600 ],
))

plotList.append( Plot(
    name      = 'j0_eta',
    texX      = '#eta(j_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Jet_eta[0]) if event.nJet > 0 else -999,
    binning   = [ 10, 0, 3 ],
))

plotList.append( Plot(
    name      = 'j0_phi',
    texX      = '#phi(j_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_phi[0] if event.nJet > 0 else -999,
    binning   = [ 10, -pi, pi ],
))

plotList.append( Plot(
    name      = 'j1_pt',
    texX      = 'p_{T}(j_{1}) (GeV)',
    texY      = 'Number of Events / 20 GeV',
    attribute = lambda event, sample: event.Jet_pt[1] if event.nJet > 1 else -999,
    binning   = [ 20, 0, 600 ],
))

plotList.append( Plot(
    name      = 'j1_eta',
    texX      = '#eta(j_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Jet_eta[1]) if event.nJet > 1 else -999,
    binning   = [ 10, 0, 3 ],
))

plotList.append( Plot(
    name      = 'j1_phi',
    texX      = '#phi(j_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_phi[1] if event.nJet > 1 else -999,
    binning   = [ 10, -pi, pi ],
))
