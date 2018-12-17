#!/usr/bin/env python
''' Analysis script for standard plots
'''

# Standard imports
import ROOT, os, imp, sys, copy
ROOT.gROOT.SetBatch(True)
import itertools
from math                             import isnan, ceil, pi

# RootTools
from RootTools.core.standard          import *

# Internal Imports
from TTGammaEFT.Tools.user            import plot_directory
from TTGammaEFT.Tools.cutInterpreter  import cutInterpreter
from TTGammaEFT.Tools.TriggerSelector import TriggerSelector

from TTGammaEFT.Tools.objectSelection import getFilterCut
from TTGammaEFT.Tools.objectSelection import nanoPlotElectronVars, nanoPlotMuonVars, nanoPlotLeptonVars, nanoPlotTauVars, nanoPlotPhotonVars, nanoPlotJetVars, nanoPlotBJetVars
from TTGammaEFT.Tools.objectSelection import nanoPlotElectronVarString, nanoPlotMuonVarString, nanoPlotLeptonVarString, nanoPlotTauVarString, nanoPlotPhotonVarString, nanoPlotJetVarString, nanoPlotBJetVarString

# Default Parameter
loggerChoices = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO', nargs='?', choices=loggerChoices,                  help="Log level for logging")
argParser.add_argument('--plot_directory',     action='store',      default='80X_TTG_ppv1_v1')
argParser.add_argument('--plotFile',           action='store',      default='all')
argParser.add_argument('--selection',          action='store',      default='dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40')
argParser.add_argument('--small',              action='store_true',                                                                    help='Run only on a small subset of the data?', )
argParser.add_argument('--noData',             action='store_true', default=False,                                                     help='also plot data?')
argParser.add_argument('--signal',             action='store',      default=None,   nargs='?', choices=[None],                         help="Add signal to plot")
argParser.add_argument('--onlyTTG',            action='store_true', default=False,                                                     help="Plot only ttG")
argParser.add_argument('--normalize',          action='store_true', default=False,                                                     help="Normalize yields" )
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
if args.normalize:       args.plot_directory += "_normalize"

# 2016 Samples
postprocessing_directory = "TTGammaEFT_PP_2016_TTG_v1/dilep/"
from TTGammaEFT.Samples.nanoTuples_Summer16_postProcessed    import *
if not args.noData:
    postprocessing_directory = "TTGammaEFT_PP_2016_TTG_v1/dilep/"
    from TTGammaEFT.Samples.nanoTuples_Run2016_05Feb2018_postProcessed import *

# Text on the plots
def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS #bf{#it{Preliminary}}' if plotData else 'CMS #bf{#it{Simulation Preliminary}}'), 
      (0.45, 0.95, '%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.65, 0.95, '%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

#scaling = { i+1:0 for i in range(len(signals)) }
scaling = { 1:0 }

# Plotting
def drawPlots( plots, mode, dataMCScale ):
    for log in [False, True]:
        plot_directory_ = os.path.join( plot_directory, 'analysisPlots', args.plot_directory, args.selection, mode, "log" if log else "lin" )

        for plot in plots:
            if not max(l[0].GetMaximum() for l in plot.histos): 
                continue # Empty plot
            postFix = " (legacy)"
            if not args.noData: 
                plot.histos[1][0].style          = styles.errorStyle( ROOT.kBlack )
                if mode == "all":
                    plot.histos[1][0].legendText = "Data" + postFix
                if mode == "SF":
                    plot.histos[1][0].legendText = "Data (SF)" + postFix
            extensions_ = ["pdf", "png", "root"] if mode in ['all', 'SF', 'mue'] else ['png']

            plotting.draw( plot,
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

def getYieldPlot( index ):
    return Plot(
                name      = 'yield',
                texX      = 'yield',
                texY      = 'Number of Events',
                attribute = lambda event, sample: 0.5 + index,
                binning   = [ 3, 0, 3 ],
                )

# Read variables and sequences
read_variables  = ["weight/F", "ref_weight/F",
                   "PV_npvs/F", "PV_npvsGood/F",
                   "nJet/I", "nAllJet/I", "nBTag/I",
                   "Jet[%s]"         %nanoPlotJetVarString,
                   "nLepton/I", "nLeptonTight/I", "nLeptonVeto/I", "nElectron/I", "nMuon/I",
                   "Lepton[%s]"      %nanoPlotLeptonVarString,
                   "nPhoton/I",
                   "Photon[%s]"      %(nanoPlotPhotonVarString),
                   "MET_pt/F", "MET_phi/F", "METSig/F", "ht/F",
                   "mll/F", "mllgamma/F",
                   "m3/F", "m3wBJet/F",
                   "lldR/F", "lldPhi/F", "bbdR/F", "bbdPhi/F",
                   "photonJetdR/F", "photonLepdR/F", "leptonJetdR/F",
                   "mL0Gamma/F",  "mL1Gamma/F",
                   "l0GammadR/F", "l0GammadPhi/F",
                   "l1GammadR/F", "l1GammadPhi/F",
                   "j0GammadR/F", "j0GammadPhi/F",
                   "j1GammadR/F", "j1GammadPhi/F",
                  ]


read_variables += [ 'Bj0_' + var for var in nanoPlotBJetVarString.split(',') ]
read_variables += [ 'Bj1_' + var for var in nanoPlotBJetVarString.split(',') ]

read_variables_MC = ["isTTGamma/I", "isZGamma/I",
                     "Photon[photonCat/I]",
#                     "GenElectron[%s]" %nanoGenVarString,
#                     "GenMuon[%s]"     %nanoGenVarString,
#                     "GenPhoton[%s]"   %nanoGenVarString,
#                     "GenJet[%s]"      %nanoGenJetVarString,
#                     "GenBJet[%s]"     %nanoGenJetVarString,
#                     "GenTop[%s]"      %nanoGenVarString,
                     "reweightPU36fb/F", "reweightPU36fbDown/F", "reweightPU36fbUp/F", "reweightPU36fbVDown/F", "reweightPU36fbVUp/F",
                     "reweightLeptonSF/F", "reweightLeptonSFUp/F", "reweightLeptonSFDown/F",
                     "reweightLeptonTrackingSF/F",
                     "reweightDilepTrigger/F", "reweightDilepTriggerUp/F", "reweightDilepTriggerDown/F",
                     "reweightDilepTriggerBackup/F", "reweightDilepTriggerBackupUp/F", "reweightDilepTriggerBackupDown/F",
                     "reweightPhotonSF/F", "reweightPhotonSFUp/F", "reweightPhotonSFDown/F",
                     "reweightPhotonElectronVetoSF/F",
                     "reweightBTag_SF/F", "reweightBTag_SF_b_Down/F", "reweightBTag_SF_b_Up/F", "reweightBTag_SF_l_Down/F", "reweightBTag_SF_l_Up/F",
                    ]

# Sequence
sequence = []

# Sample definition
if args.onlyTTG: mc = [ TTGLep ]
else:            mc = [ TTGLep, DY_LO_16 , TTbar, singleTop_16, ZGToLLG ]
#else:            mc = [ TTGLep, DY_LO_16 , TTbar, ZGToLLG ]

if args.noData:
    lumi_scale = 35.9
    stack      = Stack( mc )
else:
    data_sample                = Run2016
    data_sample.texName        = "data (legacy)"
    data_sample.name           = "data"
    data_sample.read_variables = [ "event/I", "run/I" ]
    data_sample.scale          = 1

    lumi_scale                 = data_sample.lumi * 0.001
    stack                      = Stack( mc, data_sample )

stack.extend( [ [s] for s in signals ] )

for sample in mc + signals:
    sample.read_variables = read_variables_MC
    sample.scale          = lumi_scale
    sample.style          = styles.fillStyle( sample.color )
#    sample.weight         = lambda event, sample: 1.
    sample.weight         = lambda event, sample: event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonSF*event.reweightLeptonTrackingSF*event.reweightPhotonSF*event.reweightPhotonElectronVetoSF*event.reweightBTag_SF
#    sample.weight         = lambda event, sample: event.reweightDilepTriggerBackup
#    sample.weight         = lambda event, sample: event.reweightPU36fb
#    sample.weight         = lambda event, sample: event.reweightLeptonSF
#    sample.weight         = lambda event, sample: event.reweightLeptonTrackingSF
#    sample.weight         = lambda event, sample: event.reweightPhotonSF
#    sample.weight         = lambda event, sample: event.reweightPhotonElectronVetoSF
#    sample.weight         = lambda event, sample: event.reweightBTag_SF

if args.small:
    for sample in stack.samples:
        sample.normalization=1.
        sample.reduceFiles( factor=5 )
        sample.scale /= sample.normalization

weight_ = lambda event, sample: event.weight
tr = TriggerSelector( 2016 )

# Use some defaults (set defaults before you create/import list of Plots!!)
Plot.setDefaults( stack=stack, weight=staticmethod( weight_ ), selectionString=cutInterpreter.cutString( args.selection ), addOverFlowBin='upper' )

# Import plots list (AFTER setDefaults!!)
plotListFile = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), 'plotLists', args.plotFile + '.py' )
if not os.path.isfile( plotListFile ):
    logger.info( "Plot file not found: %s", plotListFile )
    sys.exit(1)

plotModule = imp.load_source( "plotLists", os.path.expandvars( plotListFile ) )
if args.noData: from plotLists import plotListDataMC as plotList
else:           from plotLists import plotListData   as plotList

# Loop over channels
yields   = {}
allPlots = {}
allModes = [ 'mumu', 'mue', 'ee' ]

for index, mode in enumerate( allModes ):
    logger.info( "Computing plots for mode %s", mode )

    yields[mode] = {}

    # always initialize with [], elso you get in trouble with pythons references!
    plots  = []
    plots += plotList
    plots += [ getYieldPlot( index ) ]

    # Define 2l selections
    leptonSelection = cutInterpreter.cutString( mode )

    if not args.noData:    data_sample.setSelectionString( [ getFilterCut( isData=True, year=2016 ),  leptonSelection ] )
    for sample in mc + signals: sample.setSelectionString( [ getFilterCut( isData=False, year=2016 ), leptonSelection, tr.getSelection( "MC" ) ] )

    # Overlap removal
    TTGLep.addSelectionString(    "isTTGamma==1" )
#    TTG_16.addSelectionString(    "isTTGamma==1" )
#    TT_pow_16.addSelectionString( "isTTGamma==0" )
    TTbar.addSelectionString(     "isTTGamma==0" )
#    ZGTo2LG.addSelectionString(   "isZGamma==1"  )
    ZGToLLG.addSelectionString(   "isZGamma==1"  )
    DY_LO_16.addSelectionString(  "isZGamma==0"  )

    plotting.fill( plots, read_variables=read_variables, sequence=sequence )

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

    logger.info( "Plotting mode %s", mode )
    allPlots[mode] = copy.deepcopy(plots) # deep copy for creating SF/all plots afterwards!
    drawPlots( allPlots[mode], mode, dataMCScale )


# Add the different channels into SF and all
for mode in [ "SF", "all" ]:
    yields[mode] = {}

    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum( yields[c][y] for c in ( ['ee','mumu'] if mode=="SF" else ['ee','mumu','mue'] ) )
        except: yields[mode][y] = 0

    dataMCScale = yields[mode]["data"] / yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    for plot in allPlots['mumu']:
        for pl in ( p for p in ( allPlots['ee'] if mode=="SF" else allPlots["mue"] ) if p.name == plot.name ):  #For SF add EE, second round add EMu for all
            for i, j in enumerate( list( itertools.chain.from_iterable( plot.histos ) ) ):
                j.Add( list( itertools.chain.from_iterable( pl.histos ) )[i] )

    drawPlots( allPlots['mumu'], mode, dataMCScale )

