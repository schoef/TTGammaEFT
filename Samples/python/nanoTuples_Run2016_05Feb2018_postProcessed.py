# Standard Imports
import os, sys
import ROOT

# RootTools Imports
from RootTools.core.Sample import Sample 

# TTGammaEFT Imports
from TTGammaEFT.Samples.helpers import getSample, merge

# Logging
import logging
logger = logging.getLogger(__name__)

# Data directory
try:    data_directory = sys.modules['__main__'].data_directory
except: from TTGammaEFT.Tools.user import data_directory

# Take post processing directory if defined in main module
try:    postprocessing_directory = sys.modules['__main__'].postprocessing_directory
except: from TTGammaEFT.Tools.user import postprocessing_directory

logger.info("Loading data samples from directory %s", os.path.join(data_directory, postprocessing_directory))

dirs = {}
# no event that passes json in B_ver1
for ( run, version ) in [ ( 'B', '_ver2' ), ( 'C', '' ), ( 'D', '' ), ( 'E', '' ), ( 'F', '' ), ( 'G', '' ), ( 'H', '_ver2' ), ( 'H', '_ver3' ) ]:
    runTag = 'Run2016' + run + '_05Feb2018' + version
    dirs[ "DoubleEG_Run2016"   + run + version ] = ["DoubleEG_"   + runTag ]
    dirs[ "DoubleMuon_Run2016" + run + version ] = ["DoubleMuon_" + runTag ]
    dirs[ "MuonEG_Run2016"     + run + version ] = ["MuonEG_"     + runTag ]

for pd in [ 'MuonEG', 'DoubleMuon', 'DoubleEG' ]:
    merge( pd, 'Run2016BCD',    [ 'Run2016B_ver2', 'Run2016C', 'Run2016D' ], dirs )
    merge( pd, 'Run2016BCDEFG', [ 'Run2016BCD', 'Run2016E', 'Run2016F', 'Run2016G' ], dirs )
    merge( pd, 'Run2016',       [ 'Run2016BCDEFG', 'Run2016H_ver2', 'Run2016H_ver3' ], dirs )

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postprocessing_directory, dir ) for dir in dirs[key] ]

DoubleEG_Run2016   = getSample( 'DoubleEG',   'Run2016', 35.9*1000, dirs )
DoubleMuon_Run2016 = getSample( 'DoubleMuon', 'Run2016', 35.9*1000, dirs )
MuonEG_Run2016     = getSample( 'MuonEG',     'Run2016', 35.9*1000, dirs )

allSamples_Data25ns  = []
allSamples_Data25ns += [ MuonEG_Run2016, DoubleEG_Run2016, DoubleMuon_Run2016 ]

Run2016      = Sample.combine( "Run2016", [ MuonEG_Run2016, DoubleEG_Run2016, DoubleMuon_Run2016 ], texName = "Data" )
Run2016.lumi = (35.9)*1000

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True
