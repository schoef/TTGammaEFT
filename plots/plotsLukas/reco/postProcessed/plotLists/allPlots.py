#!/usr/bin/env python
''' Define list of plots for plot script
'''

# RootTools
from RootTools.core.standard          import *

# Plots
plots = []
    
plots.append( Plot(
  name = 'yield',
  texX = 'yield',
  texY = 'Number of Events',
  attribute = lambda event, sample: 0.5 + index,
  binning=[ 3, 0, 3 ],
))
    
plots.append( Plot(
    name = 'Photon_pT',
    texX = 'p_{T}(#gamma) (GeV)',
    texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "Photon_pt/F" ),
    binning=[ 20, 0, 400 ],
))

