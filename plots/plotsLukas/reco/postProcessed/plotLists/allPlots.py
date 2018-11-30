#!/usr/bin/env python
''' Define list of plots for plot script
'''

# Standard Imports
from math                             import pi

# RootTools
from RootTools.core.standard          import *

# plotList
plotList = []
    
#plotList.append( Plot(
#    name      = 'dRL0Gamma',
#    texX      = '#DeltaR(#gamma,l_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.l0GammadR if event.nPhoton >= 1 and event.nLepton >= 1 else -999,
#    binning   = [ 40, 0, 4 ],
#))

#plotList.append( Plot(
#    name      = 'dPhiL0Gamma',
#    texX      = '#Delta#phi(#gamma,l_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.l0GammadPhi if event.nPhoton >= 1 and event.nLepton >= 1 else -999,
#    binning   = [ 40, 0, pi ],
#))

#plotList.append( Plot(
#    name      = 'dRL1Gamma',
#    texX      = '#DeltaR(#gamma,l_{1})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.l1GammadR if event.nPhoton >= 1 and event.nLepton >= 2 else -999,
#    binning   = [ 40, 0, 4 ],
#))

#plotList.append( Plot(
#    name      = 'dPhiL1Gamma',
#    texX      = '#Delta#phi(#gamma,l_{1})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.l1GammadPhi if event.nPhoton >= 1 and event.nLepton >= 2 else -999,
#    binning   = [ 40, 0, pi ],
#))

#plotList.append( Plot(
#    name      = 'dRJ0Gamma',
#    texX      = '#DeltaR(#gamma,j_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.j0GammadR if event.nPhoton >= 1 and event.nJet >= 1 else -999,
#    binning   = [ 40, 0, 4 ],
#))

#plotList.append( Plot(
#    name      = 'dPhiJ0Gamma',
#    texX      = '#Delta#phi(#gamma,j_{0})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.j0GammadPhi if event.nPhoton >= 1 and event.nJet >= 1 else -999,
#    binning   = [ 40, 0, pi ],
#))

#plotList.append( Plot(
#    name      = 'dRJ1Gamma',
#    texX      = '#DeltaR(#gamma,j_{1})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.j1GammadR if event.nPhoton >= 1 and event.nJet >= 2 else -999,
#    binning   = [ 40, 0, 4 ],
#))

#plotList.append( Plot(
#    name      = 'dPhiJ1Gamma',
#    texX      = '#Delta#phi(#gamma,j_{1})',
#    texY      = 'Number of Events',
#    attribute = lambda event, sample: event.j1GammadPhi if event.nPhoton >= 1 and event.nJet >= 2 else -999,
#    binning   = [ 40, 0, pi ],
#))

plotList.append( Plot(
    name      = 'mindRJetGamma',
    texX      = 'min(#DeltaR(#gamma_{0}, jet))',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.photonJetdR if event.nJet >= 1 and event.nPhoton >= 1 else -999,
    binning   = [ 40, 0, 4 ],
))

plotList.append( Plot(
    name      = 'mindRLepGamma',
    texX      = 'min(#DeltaR(#gamma_{0}, l))',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.photonLepdR if event.nLepton >= 1 and event.nPhoton >= 1 else -999,
    binning   = [ 40, 0, 4 ],
))

plotList.append( Plot(
    name      = 'dRll',
    texX      = '#DeltaR(ll)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.lldR if event.nLepton >= 2 else -999,
    binning   = [ 40, 0, 4 ],
))

plotList.append( Plot(
    name      = 'dPhill',
    texX      = '#Delta#phi(ll)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.lldPhi if event.nLepton >= 2 else -999,
    binning   = [ 40, 0, pi ],
))

plotList.append( Plot(
    name      = 'dRbb',
    texX      = '#DeltaR(bb)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.bbdR if event.nBTag >= 2 else -999,
    binning   = [ 40, 0, 4 ],
))

plotList.append( Plot(
    name      = 'dPhibb',
    texX      = '#Delta#phi(bb)',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.bbdPhi if event.nBTag >= 2 else -999,
    binning   = [ 40, 0, pi ],
))

#plotList.append( Plot(
#    name      = 'mL0Gamma',
#    texX      = 'M(#gamma,l_{0]) (GeV)',
#    texY      = 'Number of Events / 4 GeV',
#    attribute = lambda event, sample: event.mL0Gamma if event.nLepton >= 1 and event.nPhoton >= 1 else -999,
#    binning   = [ 35, 60, 200 ],
#))

#plotList.append( Plot(
#    name      = 'mL1Gamma',
#    texX      = 'M(#gamma,l_{1]) (GeV)',
#    texY      = 'Number of Events / 4 GeV',
#    attribute = lambda event, sample: event.mL1Gamma if event.nLepton >= 2 and event.nPhoton >= 1 else -999,
#    binning   = [ 35, 60, 200 ],
#))

plotList.append( Plot(
    name      = 'mll',
    texX      = 'M(ll) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mll if event.nLepton >= 2 else -999,
    binning   = [ 50, 0, 200 ],
))

plotList.append( Plot(
    name      = 'mllgamma',
    texX      = 'M(ll#gamma) (GeV)',
    texY      = 'Number of Events / 4 GeV',
    attribute = lambda event, sample: event.mllgamma if event.nLepton >= 2 else -999,
    binning   = [ 50, 0, 200 ],
))

plotList.append( Plot(
    name      = 'm3',
    texX      = 'M_{3} (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.m3 if event.nJet >= 3 else -999,
    binning   = [ 20, 50, 250 ],
))

plotList.append( Plot(
    name      = 'm3wBJet',
    texX      = 'M_{3} w/ #geq 1 BJet (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.m3wBJet if event.nJet >= 3 and event.nBTag >= 1 else -999,
    binning   = [ 20, 50, 250 ],
))

plotList.append( Plot(
    name      = 'MET_pt',
    texX      = 'E^{miss}_{T} (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.MET_pt,
    binning   = [ 20, 0, 200 ],
))

plotList.append( Plot(
    name      = 'MET_phi',
    texX      = '#phi(E^{miss}_{T})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.MET_phi,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'gamma0_pt',
    texX      = 'p_{T}(#gamma_{0}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.Photon_pt[0] if event.nPhoton > 0 else -999,
    binning   = [ 19, 20, 115 ],
))

plotList.append( Plot(
    name      = 'gamma0_eta',
    texX      = '#eta(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_eta[0] if event.nPhoton > 0 else -999,
    binning   = [ 20, -1.5, 1.5 ],
))

plotList.append( Plot(
    name      = 'gamma0_absEta',
    texX      = '|#eta|(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Photon_eta[0]) if event.nPhoton > 0 else -999,
    binning   = [ 9, 0, 1.5 ],
))

plotList.append( Plot(
    name      = 'gamma0_phi',
    texX      = '#phi(#gamma_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_phi[0] if event.nPhoton > 0 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'gamma1_pt',
    texX      = 'p_{T}(#gamma_{1}) (GeV)',
    texY      = 'Number of Events / 5 GeV',
    attribute = lambda event, sample: event.Photon_pt[1] if event.nPhoton > 1 else -999,
    binning   = [ 19, 20, 115 ],
))

plotList.append( Plot(
    name      = 'gamma1_eta',
    texX      = '#eta(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_eta[1] if event.nPhoton > 1 else -999,
    binning   = [ 20, -1.5, 1.5 ],
))

plotList.append( Plot(
    name      = 'gamma1_absEta',
    texX      = '|#eta|(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: abs(event.Photon_eta[1]) if event.nPhoton > 1 else -999,
    binning   = [ 9, 0, 1.5 ],
))

plotList.append( Plot(
    name      = 'gamma1_phi',
    texX      = '#phi(#gamma_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_phi[1] if event.nPhoton > 1 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'l0_pt',
    texX      = 'p_{T}(l_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Lepton_pt[0] if event.nLepton > 0 else -999,
    binning   = [ 20, 0, 200 ],
))

plotList.append( Plot(
    name      = 'l0_eta',
    texX      = '#eta(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_eta[0] if event.nLepton > 0 else -999,
    binning   = [ 20, -2.5, 2.5 ],
))

plotList.append( Plot(
    name      = 'l0_phi',
    texX      = '#phi(l_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_phi[0] if event.nLepton > 0 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'l1_pt',
    texX      = 'p_{T}(l_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Lepton_pt[1] if event.nLepton > 1 else -999,
    binning   = [ 20, 0, 200 ],
))

plotList.append( Plot(
    name      = 'l1_eta',
    texX      = '#eta(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_eta[1] if event.nLepton > 1 else -999,
    binning   = [ 20, -2.5, 2.5 ],
))

plotList.append( Plot(
    name      = 'l1_phi',
    texX      = '#phi(l_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Lepton_phi[1] if event.nLepton > 1 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'j0_pt',
    texX      = 'p_{T}(j_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Jet_pt[0] if event.nJet > 0 else -999,
    binning   = [ 20, 0, 200 ],
))

plotList.append( Plot(
    name      = 'j0_eta',
    texX      = '#eta(j_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[0] if event.nJet > 0 else -999,
    binning   = [ 20, -2.5, 2.5 ],
))

plotList.append( Plot(
    name      = 'j0_phi',
    texX      = '#phi(j_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_phi[0] if event.nJet > 0 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'j1_pt',
    texX      = 'p_{T}(j_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Jet_pt[1] if event.nJet > 1 else -999,
    binning   = [ 20, 0, 200 ],
))

plotList.append( Plot(
    name      = 'j1_eta',
    texX      = '#eta(j_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_eta[1] if event.nJet > 1 else -999,
    binning   = [ 20, -2.5, 2.5 ],
))

plotList.append( Plot(
    name      = 'j1_phi',
    texX      = '#phi(j_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Jet_phi[1] if event.nJet > 1 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'bj0_pt',
    texX      = 'p_{T}(b_{0}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Bj0_pt if event.nBTag > 0 else -999,
    binning   = [ 20, 0, 200 ],
))

plotList.append( Plot(
    name      = 'bj0_eta',
    texX      = '#eta(b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj0_eta if event.nBTag > 0 else -999,
    binning   = [ 20, -2.5, 2.5 ],
))

plotList.append( Plot(
    name      = 'bj0_phi',
    texX      = '#phi(b_{0})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj0_phi if event.nBTag > 0 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'bj1_pt',
    texX      = 'p_{T}(b_{1}) (GeV)',
    texY      = 'Number of Events / 10 GeV',
    attribute = lambda event, sample: event.Bj1_pt if event.nBTag > 1 else -999,
    binning   = [ 20, 0, 200 ],
))

plotList.append( Plot(
    name      = 'bj1_eta',
    texX      = '#eta(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj1_eta if event.nBTag > 1 else -999,
    binning   = [ 20, -2.5, 2.5 ],
))

plotList.append( Plot(
    name      = 'bj1_phi',
    texX      = '#phi(b_{1})',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Bj1_phi if event.nBTag > 1 else -999,
    binning   = [ 20, -pi, pi ],
))

plotList.append( Plot(
    name      = 'nPhoton',
    texX      = 'N_{#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nPhoton,
    binning   = [ 3, 0, 3 ],
))

plotList.append( Plot(
    name      = 'nLepton',
    texX      = 'N_{l}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nLepton,
    binning   = [ 4, 0, 4 ],
))

plotList.append( Plot(
    name      = 'nElectron',
    texX      = 'N_{e}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nElectron,
    binning   = [ 4, 0, 4 ],
))

plotList.append( Plot(
    name      = 'nMuon',
    texX      = 'N_{#mu}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nMuon,
    binning   = [ 4, 0, 4 ],
))

plotList.append( Plot(
    name      = 'nJet',
    texX      = 'N_{jet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nJet,
    binning   = [ 7, 0, 7 ],
))

plotList.append( Plot(
    name      = 'nBJet',
    texX      = 'N_{bJet}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.nBTag,
    binning   = [ 4, 0, 4 ],
))

plotList.append( Plot(
    name      = 'isTTG',
    texX      = 'Flag_{tt#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isTTGamma,
    binning   = [ 2, 0, 2 ],
))

plotList.append( Plot(
    name      = 'isZG',
    texX      = 'Flag_{Z#gamma}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.isZGamma,
    binning   = [ 2, 0, 2 ],
))

plotList.append( Plot(
    name      = 'gamma0_category',
    texX      = 'Category_{#gamma_{0}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_photonCat[0],
    binning   = [ 4, 0, 4 ],
))

plotList.append( Plot(
    name      = 'gamma1_category',
    texX      = 'Category_{#gamma_{1}}',
    texY      = 'Number of Events',
    attribute = lambda event, sample: event.Photon_photonCat[1],
    binning   = [ 4, 0, 4 ],
))

