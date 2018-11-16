#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp
ROOT.gROOT.SetBatch(True)
import itertools
from math                             import isnan, pi

# RootTools
from RootTools.core.standard          import *

# Internal Imports
from TTGammaEFT.Tools.user            import plot_directory
#from TTGammaEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, deltaR, deltaR2
from TTGammaEFT.Tools.cutInterpreter  import cutInterpreter
from TTGammaEFT.Tools.triggerSelector import triggerSelector

from TTGammaEFT.Tools.objectSelection import getFilterCut
from TTGammaEFT.Tools.objectSelection import nanoElectronVars, nanoMuonVars, nanoLeptonVars, nanoTauVars, nanoPhotonVars, nanoJetVars, nanoGenVars, nanoGenJetVars
from TTGammaEFT.Tools.objectSelection import nanoElectronVarString, nanoMuonVarString, nanoLeptonVarString, nanoTauVarString, nanoPhotonVarString, nanoJetVarString, nanoGenVarString, nanoBJetVars, nanoBJetVarString, nanoGenJetVarString

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                  help="Log level for logging")
argParser.add_argument('--plot_directory',     action='store',      default='94X_TTG_v1')
argParser.add_argument('--selection',          action='store',      default='dilepOS-pTG20-nPhoton1p-offZSF-mll40-nJet3p-nBTag1p')
argParser.add_argument('--useNanoAODSamples',   action='store_true',                                                                    help='Use the original nanoAOD samples', )
argParser.add_argument('--small',              action='store_true',                                                                    help='Run only on a small subset of the data?', )
argParser.add_argument('--noData',             action='store_true', default=False,                                                     help='also plot data?')
argParser.add_argument('--signal',             action='store',      default=None,   nargs='?', choices=[None, "ewkDM", "ttZ01j"],      help="Add signal to plot")
argParser.add_argument('--onlyTTG',            action='store_true', default=False,                                                     help="Plot only ttG")
argParser.add_argument('--TTZ_LO',             action='store_true',                                                                    help='Use LO TTZ?', )
argParser.add_argument('--normalize',          action='store_true', default=False,                                                     help="Normalize yields" )
argParser.add_argument('--reweightPtZToSM',    action='store_true',                                                                    help='Reweight Pt(Z) to the SM for all the signals?', )
args = argParser.parse_args()

# Logger
import TTGammaEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:           args.plot_directory += "_small"
if args.noData:          args.plot_directory += "_noData"
if args.signal:          args.plot_directory += "_signal_"+args.signal
if args.onlyTTG:         args.plot_directory += "_onlyTTG"
if args.TTZ_LO:          args.plot_directory += "_TTZ_LO"
if args.normalize:       args.plot_directory += "_normalize"
if args.reweightPtZToSM: args.plot_directory += "_reweightPtZToSM"


# Make samples, will be searched for in the postProcessing directory
# 2016
if args.useNanoAODSamples:
    from Samples.nanoAOD.Summer16          import *
    from Samples.nanoAOD.Run2016_05Feb2018 import *

else:
    data_directory = "/afs/hephy.at/data/llechner01/nanoTuples/"
    postprocessing_directory = "TTGammaEFT_PP_2016_TTG_v1/dilep/"
    from TTGammaEFT.Samples.nanoTuples_Summer16_postProcessed    import *

    data_directory = "/afs/hephy.at/data/llechner01/nanoTuples/"
    postprocessing_directory = "TTGammaEFT_PP_2016_TTG_v1/dilep/"
    from TTGammaEFT.Samples.nanoTuples_Data25ns_xxx_postProcessed import *

# 2017
#data_directory = "/afs/hephy.at/data/llechner01/nanoTuples/"
#postprocessing_directory = "TTGammaEFT_PP_2017_TTG_v1/dilep/"
#from TTGammaEFT.Samples.nanoTuples_Fall17_postProcessed      import *

#data_directory = "/afs/hephy.at/data/llechner01/nanoTuples/"
#postprocessing_directory = "TTGammaEFT_PP_2017_TTG_v1/dilep/"
#from TTGammaEFT.Samples.cmgTuples_Data25ns_xxx_postProcessed import *

# Text on the plots
def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

#scaling = { i+1:0 for i in range(len(signals)) }
scaling = { 1:0 }

# Plotting
def drawPlots(plots, mode, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      postFix = " (legacy)"
      if not args.noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data" + postFix
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)" + postFix
      extensions_ = ["pdf", "png", "root"] if mode == 'all' else ['png']

      plotting.draw(plot,
	    plot_directory = plot_directory_,
        extensions = extensions_,
	    ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = scaling if args.normalize else {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ) if not args.normalize else drawObjects( not args.noData, 1.0 , lumi_scale ),
        copyIndexPHP = True,
      )

# Reweighting 
if args.reweightPtZToSM:
    sel_string = "&&".join( [ getFilterCut( isData=False, year=2016 ), getLeptonSelection( 'all' ), cutInterpreter.cutString( args.selection ) ] )
    TTZ_ptZ = TTZtoLLNuNu.get1DHistoFromDraw("Z_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
    TTZ_ptZ.Scale(1./TTZ_ptZ.Integral())

    def get_reweight( var, histo ):

        def reweight(event, sample):
            i_bin = histo.FindBin(getattr( event, var ) )
            return histo.GetBinContent(i_bin)

        return reweight

    for signal in signals:
        logger.info( "Computing PtZ reweighting for signal %s", signal.name )
        signal_ptZ = signal.get1DHistoFromDraw( "Z_pt", [20,0,1000], selectionString=sel_string, weightString="weight" )
        signal_ptZ.Scale( 1./signal_ptZ.Integral() )

        signal.reweight_ptZ_histo = TTZ_ptZ.Clone()
        signal.reweight_ptZ_histo.Divide( signal_ptZ )

        signal.weight = get_reweight( "Z_pt", signal.reweight_ptZ_histo )

# Read variables and sequences
read_variables  = ["weight/F", "ref_weight/F",
                   "Jet[%s]"         %nanoJetVars, "nJet/I", "nAllJet/I", "nBTag/I",
                   "Lepton[%s]"      %nanoLeptonVars, "nLepton/I", "nLeptonTight/I", "nLeptonVeto/I", "nElectron/I", "nMuon/I"
                   "Photon[%s]"      %nanoPhotonVars, "nPhoton/I",
                   "GenElectron[%s]" %nanoGenVarString,
                   "GenMuon[%s]"     %nanoGenVarString,
                   "GenPhoton[%s]"   %nanoGenVarString,
                   "GenJet[%s]"      %nanoGenJetVarString,
                   "GenBJet[%s]"     %nanoGenJetVarString,
                   "GenTop[%s]"      %nanoGenVarString,
                   "MET_pt/F", "MET_phi/F", "METSig/F", "ht/F",
                   "mll/F", "mllgamma/F",
                   "lldR/F", "lldPhi/F", "bbdR/F", "bbdPhi/F",
                   "photonJetdR/F", "photonLepdR/F",
                   "isTTGamma/I", "isZGamma/I",
                  ]

read_variables += [ 'Bj0_' + var for var in nanoBJetVarString.split(',') ]
read_variables += [ 'Bj1_' + var for var in nanoBJetVarString.split(',') ]

# Sequence
sequence = []

# Import plots list
plotListFile = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'plotLists', 'allPlots.py' )
plots        = imp.load_source( "plots", os.path.expandvars( plotListFile ) ).plots

# Sample definition
#if args.TTZ_LO:   TTZ_mc = TTZ_LO
#else:             TTZ_mc = TTZtoLLNuNu
TTG_mc = TTGJets_ext

if   args.useNanoAODSamples and args.onlyTTG: mc = [ TTGJets_ext ]
elif args.useNanoAODSamples:                  mc = [ TTGJets_ext,  ]
elif args.onlyTTG:                            mc = [ TTG_mc ]
else:                                         mc = [ TTG_mc,  ]

if args.noData:
    lumi_scale = 35.9
    stack = Stack( mc, [ [s] for s in signals ] )
else:
    data_sample = Run2016
    data_sample.texName = "data (legacy)"
    data_sample.name           = "data"
    data_sample.read_variables = [ "evt/I", "run/I" ]
    data_sample.style          = styles.errorStyle( ROOT.kBlack )
    lumi_scale                 = data_sample.lumi * 0.001
    stack = Stack( mc, data_sample, [ [s] for s in signals ] )

if args.small:
    for sample in stack.samples:
        sample.reduceFiles( to = 1 )

for sample in mc + signals:
    if sample in mc: sample.style = styles.fillStyle( sample.color )
    sample.scale          = lumi_scale
    sample.read_variables = [] # add SF
    sample.weight         = lambda event, sample: 1.
#    sample.read_variables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F', 'reweightLeptonSFSyst_tight_3l/F', 'reweightLeptonTrackingSF_tight_3l/F', 'reweightTrigger_tight_3l/F', "Z_pt/F"]
#    sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightPU36fb*event.reweightLeptonSFSyst_tight_3l*event.reweightLeptonTrackingSF_tight_3l*event.reweightTrigger_tight_3l

# Use some defaults
Plot.setDefaults( stack=stack, weight=staticmethod( weight_ ), selectionString=cutInterpreter.cutString( args.selection ), addOverFlowBin='upper' )
plotting.fill( plots, read_variables=read_variables, sequence=sequence )

weight_ = lambda event, sample: event.weight
tr = triggerSelector( 2016 )

# Loop over channels
yields   = {}
allPlots = {}
allModes = [ 'mumu', 'mue', 'ee' ]

for index, mode in enumerate( allModes ):
    yields[mode] = {}

    # Define 2l selections ( mumu, mue, ee, all )
    leptonSelection = cutInterpreter.cutString( mode )

    if not args.noData: data_sample.setSelectionString( [ getFilterCut( isData=True, year=2016 ), leptonSelection ] )

    for sample in mc + signals:
        sample.setSelectionString( [ getFilterCut( isData=False, year=2016 ), leptonSelection, tr.getSelection( "MC" ) ] )

    # Use some defaults
#    Plot.setDefaults( stack=stack, weight=staticmethod( weight_ ), selectionString=cutInterpreter.cutString( args.selection ), addOverFlowBin='upper' )
#    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

    # Get normalization yields from yield histogram
    for plot in plots:
        if plot.name != "yield": continue
        for i, l in enumerate( plot.histos ):
          for j, h in enumerate( l ):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent( h.FindBin( 0.5+index ) )
            h.GetXaxis().SetBinLabel( 1, "#mu#mu" )
            h.GetXaxis().SetBinLabel( 2, "#mue" )
            h.GetXaxis().SetBinLabel( 3, "ee" )
    if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum( yields[mode][s.name] for s in mc )
    dataMCScale        = yields[mode]["data"] / yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots( plots, mode, dataMCScale )
    allPlots[mode] = plots

# Total data/MC scale
totalDataYield = sum( yields[m]["data"] for m in allModes )
totalMCYield   = sum( yields[m]["MC"]   for m in allModes )
dataMCScale = totalDataYield / totalMCYield if totalMCYield != 0 else float('nan')

# Add plots of different channels into "all"
for plot0 in allPlots[allModes[0]]: # get all plots (no matter which mode)
    histoList0 = list( itertools.chain.from_iterable( plot0.histos ) )
    # Loop over all histos, to add other yields
    for i_hi, hi in enumerate( histoList0 ):
        # Loop over all modes, to add other yields
        for mode in allModes[1:]:
            specificPlotHistos = allPlots[mode][plot0.name].histos
            specificHisto      = list( itertools.chain.from_iterable( specificPlotHistos ) )[i_hi]
            hi.Add( specificHisto )

drawPlots( allPlots[allModes[0]], "all", dataMCScale )

