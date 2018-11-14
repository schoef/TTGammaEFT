#!/usr/bin/env python

# standard imports
import ROOT
import sys
import os
import copy
import random
import subprocess
import datetime
import shutil
import uuid

from array import array
from operator import mul
from math import sqrt, atan2, sin, cos, cosh, isnan

# RootTools
from RootTools.core.standard import *

# User specific
import TTGammaEFT.Tools.user as user

# Tools for systematics
from TTGammaEFT.Tools.helpers                    import checkRootFile, deltaR, deltaPhi, bestDRMatchInCollection

from TTGammaEFT.Tools.objectSelection            import particlePtEtaSelection, jetLeptonCleaning
from TTGammaEFT.Tools.objectSelection            import getLeptons, getGoodLeptons, getSortedParticles, getSortedParticles, getGoodParticles
from TTGammaEFT.Tools.objectSelection            import filterBJets, filterGenElectrons, filterGenMuons, filterGenPhotons, filterGenTops, filterGenBJets 
from TTGammaEFT.Tools.objectSelection            import jetSelector, muonSelector, eleSelector, photonSelector, genJetSelector, genLeptonSelector, genPhotonSelector
from TTGammaEFT.Tools.objectSelection            import nanoElectronVars, nanoMuonVars, nanoTauVars, nanoPhotonVars, nanoJetVars, nanoGenVars, nanoGenJetVars
from TTGammaEFT.Tools.objectSelection            import nanoElectronVarString, nanoMuonVarString, nanoTauVarString, nanoPhotonVarString, nanoJetVarString, nanoGenVarString, nanoBJetVars, nanoBJetVarString, nanoGenJetVarString

from TTGammaEFT.Tools.overlapRemovalTTG          import hasMesonMother, getParentIds, isTTGammaPhoton, isZGammaPhoton, isIsolatedPhoton, getPhotonCategory

from TTGammaEFT.Tools.WeightInfo                 import WeightInfo
from TTGammaEFT.Tools.HyperPoly                  import HyperPoly

# central configuration
targetLumi = 1000 #pb-1 Which lumi to normalize to

logChoices      = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET', 'SYNC']

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--logLevel',                    action='store',         nargs='?',              choices=logChoices,     default='INFO',                     help="Log level for logging")
    argParser.add_argument('--overwrite',                   action='store_true',                                                                                        help="Overwrite existing output files, bool flag set to True  if used")
    argParser.add_argument('--samples',                     action='store',         nargs='*',  type=str,                           default=['WZTo3LNu'],               help="List of samples to be post-processed, given as CMG component name")
    argParser.add_argument('--eventsPerJob',                action='store',         nargs='?',  type=int,                           default=300000000,                   help="Maximum number of events per job (Approximate!).") # mul by 100
    argParser.add_argument('--nJobs',                       action='store',         nargs='?',  type=int,                           default=1,                          help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',                         action='store',                     type=int,                           default=0,                          help="Run only job i")
    argParser.add_argument('--minNJobs',                    action='store',         nargs='?',  type=int,                           default=1,                          help="Minimum number of simultaneous jobs.")
    argParser.add_argument('--fileBasedSplitting',          action='store_true',                                                                                        help="Split njobs according to files")
    argParser.add_argument('--dataDir',                     action='store',         nargs='?',  type=str,                           default="/a/b/c",                   help="Name of the directory where the input data is stored (for samples read from Heppy).")
    argParser.add_argument('--targetDir',                   action='store',         nargs='?',  type=str,                           default=user.nanopostprocessing_output_directory, help="Name of the directory the post-processed files will be saved")
    argParser.add_argument('--processingEra',               action='store',         nargs='?',  type=str,                           default='TTGammaEFT_PP_v4',             help="Name of the processing era")
    argParser.add_argument('--skim',                        action='store',         nargs='?',  type=str,                           default='dilepTiny',                help="Skim conditions to be applied for post-processing")
    argParser.add_argument('--sync',                        action='store_true',                                                                                        help="Run syncing.")
    argParser.add_argument('--small',                       action='store_true',                                                                                        help="Run the file on a small sample (for test purpose), bool flag set to True if used")
    argParser.add_argument('--year',                        action='store',                     type=int,   choices=[2016,2017],    required = True,                    help="Which year?")
    argParser.add_argument('--addReweights',                action='store_true',                                                                                        help="Add reweights for sample EFT reweighting?")
    argParser.add_argument('--interpolationOrder',          action='store',         nargs='?',  type=int,                           default=2,                          help="Interpolation order for EFT weights.")

    return argParser

options = get_parser().parse_args()

# Logging
import TTGammaEFT.Tools.logger as logger
logFile = '/tmp/%s_%s_%s_njob%s.txt'%(options.skim, '_'.join(options.samples), os.environ['USER'], str(0 if options.nJobs==1 else options.job) )
logger  = logger.get_logger(options.logLevel, logFile = logFile, add_sync_level = options.sync)

import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )

writeToDPM = options.targetDir == '/dpm/'

#Samples: Load samples
maxN = 100 if options.small else None
if options.small:
    options.job = 1
    options.nJobs = 100 # set high to just run over 1 input file

if options.year == 2016:
    from Samples.nanoAOD.Summer16 import *
elif options.year == 2017:
    from Samples.nanoAOD.Fall17   import *

# Load all samples to be post processed
samples = map( eval, options.samples ) 
    
if len(samples)==0:
    logger.info( "No samples found. Was looking for %s. Exiting" % options.samples )
    sys.exit(-1)

isData = False not in [s.isData for s in samples]
isMC   = True not in [s.isData for s in samples]

# Check that all samples which are concatenated have the same x-section.
assert isData or len(set([s.xSection for s in samples]))==1, "Not all samples have the same xSection: %s !"%(",".join([s.name for s in samples]))
assert isMC or len(samples)==1, "Don't concatenate data samples"

skimConds = ["(1)"]
#if isSingleLep:
#    skimConds.append( "Sum$(LepGood_pt>20&&abs(LepGood_eta)<2.4) + Sum$(LepOther_pt>20&&abs(LepOther_eta)<2.5)>=1" )
#elif isDiLep:
#    skimConds.append( "Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.4) + Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5)>=2" )

# Trigger selection
from TTGammaEFT.Tools.triggerSelector import triggerSelector
ts           = triggerSelector(options.year)
triggerCond  = ts.getSelection(options.samples[0] if isData else "MC")
treeFormulas = {"triggerDecision": {'string':triggerCond} }
if isData and options.triggerSelection:
    logger.info("Sample will have the following trigger skim: %s"%triggerCond)
    skimConds.append( triggerCond )

#Samples: combine if more than one
if len(samples)>1:
    sample_name =  samples[0].name+"_comb"
    logger.info( "Combining samples %s to %s.", ",".join(s.name for s in samples), sample_name )
    sample = Sample.combine(sample_name, samples, maxN = maxN)
    # Clean up
    for s in samples:
        sample.clear()
elif len(samples)==1:
    sample = samples[0]

# Cross section for postprocessed sample
xSection = samples[0].xSection if isMC else None

# Single file post processing
if options.fileBasedSplitting:
    len_orig = len(sample.files)
    sample = sample.split( n=options.nJobs, nSub=options.job)
    if sample is None:  
        logger.info( "No such sample. nJobs %i, job %i numer of files %i", options.nJobs, options.job, len_orig )
        sys.exit(0)
    logger.info( "fileBasedSplitting: Run over %i/%i files for job %i/%i."%(len(sample.files), len_orig, options.job, options.nJobs))
    logger.debug( "fileBasedSplitting: Files to be run over:\n%s", "\n".join(sample.files) )

# output directory (store temporarily when running on dpm)
if writeToDPM:
    # Allow parallel processing of N threads on one worker
    directory = os.path.join( '/tmp/%s'%os.environ['USER'], str(uuid.uuid4()), options.processingEra )
    from TTGammaEFT.Tools.user import dpm_directory as user_dpm_directory
else:
    directory  = os.path.join( options.targetDir, options.processingEra ) 

postfix = '_small' if options.small else ''
output_directory = os.path.join( directory, options.skim+postfix, sample.name )

if os.path.exists( output_directory ) and options.overwrite:
    if options.nJobs > 1:
        logger.warning( "NOT removing directory %s because nJobs = %i", output_directory, options.nJobs )
    else:
        logger.info( "Output directory %s exists. Deleting.", output_directory )
        shutil.rmtree( output_directory, ignore_errors=True )

if not os.path.exists( output_directory ):
    os.makedirs( output_directory )
    logger.info( "Created output directory %s.", output_directory )


#branches to be kept for data and MC
branchKeepStrings_DATAMC = [\
    "run", "luminosityBlock", "event", "fixedGridRhoFastjetAll", "PV_npvs", "PV_npvsGood",
    "MET_MetUnclustEnUpDeltaX", "MET_MetUnclustEnUpDeltaY", "MET_sumEt", "CaloMET_phi", "CaloMET_pt", "CaloMET_sumEt", "MET_covXX", "MET_covXY", "MET_covYY", "MET_significance",
    "MET_phi", "MET_pt",
    "RawMET_phi", "RawMET_pt", "RawMET_sumEt",
    "Flag_*","HLT_*",
]

#branches to be kept for MC samples only
branchKeepStrings_MC = [\
    "Generator_*", "GenPart_*", "nGenPart", "genWeight", "Pileup_nTrueInt",
]

#branches to be kept for data only
branchKeepStrings_DATA = [ ]

# Branches to be kept for data and MC
# Electron variables to be read from chain
#branchKeepStrings_DATAMC += [ 'nElectron' ]
#branchKeepStrings_DATAMC += [ 'Electron_'+item for item in nanoElectronVars ]
# Muon variables to be read from chain
#branchKeepStrings_DATAMC += [ 'nMuon' ]
#branchKeepStrings_DATAMC += [ 'Muon_'+item for item in nanoMuonVars ]
# Tau variables to be read from chain
#branchKeepStrings_DATAMC += [ 'nTau' ]
#branchKeepStrings_DATAMC += [ 'Tau_'+item for item in nanoTauVars ]
# Photon variables to be read from chain
#branchKeepStrings_DATAMC += [ 'nPhoton' ]
#branchKeepStrings_DATAMC += [ 'Photon_'+item for item in nanoPhotonVars if item != 'cutBased' ]
# Jet variables to be read from chain
#branchKeepStrings_DATAMC += [ 'nJet' ]
#branchKeepStrings_DATAMC += [ 'Jet_'+item for item in nanoJetVars ]

if sample.isData:
    lumiScaleFactor=None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_DATA
    from FWCore.PythonUtilities.LumiList import LumiList
    # Apply golden JSON
    if options.year == 2016:
        json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    elif options.year == 2017:
        json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
    lumiList = LumiList(os.path.expandvars(json))
    logger.info( "Loaded json %s", json )
else:
    lumiScaleFactor = xSection*targetLumi/float(sample.normalization) if xSection is not None else None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_MC

# change in the var naming for different years
nanoPhotonVarString = nanoPhotonVarString if (not options.year == 2017) else nanoPhotonVarString.replace('cutBased','cutBasedBitmap')
nanoPhotonVars = nanoPhotonVars if (not options.year == 2017) else [ item if item != 'cutBased' else 'cutBasedBitmap' for item in nanoPhotonVars ]

# Read Variables
read_variables = map( TreeVariable.fromString, ['run/I', 'luminosityBlock/I', 'event/l'] )
read_variables = map( TreeVariable.fromString, ['PV_npvs/I', 'PV_npvsGood/I'] )
read_variables = map( TreeVariable.fromString, ['MET_pt/F', 'MET_phi/F'] )
read_variables += [ TreeVariable.fromString('nElectron/I'),
                    VectorTreeVariable.fromString('Electron[%s]'%nanoElectronVarString) ]
read_variables += [ TreeVariable.fromString('nMuon/I'),
                    VectorTreeVariable.fromString('Muon[%s]'%nanoMuonVarString) ]
read_variables += [ TreeVariable.fromString('nPhoton/I'),
                    VectorTreeVariable.fromString('Photon[%s]'%nanoPhotonVarString) ]
read_variables += [ TreeVariable.fromString('nJet/I'),
                    VectorTreeVariable.fromString('Jet[%s]'%nanoJetVarString) ]
if isMC:
    read_variables += [ TreeVariable.fromString('Pileup_nTrueInt/F') ]
    read_variables += [ TreeVariable.fromString('nGenPart/I'),
                        VectorTreeVariable.fromString('GenPart[%s]'%nanoGenVarString) ]
    read_variables += [ TreeVariable.fromString('nGenJet/I'),
                        VectorTreeVariable.fromString('GenJet[%s]'%nanoGenJetVarString) ]
    read_variables += [ TreeVariable.fromString('genWeight/F') ]


# Load reweight pickle file if supposed to keep weights. 
reweight_variables = []
if options.addReweights and isMC:

    # Determine coefficients for storing in vector
    # Sort Ids wrt to their position in the card file

    weightInfo = WeightInfo( sample.reweight_pkl )

    # weights for the ntuple
    rw_vector       = TreeVariable.fromString( "rw[w/F,"+",".join(w+'/F' for w in weightInfo.variables)+"]")
    rw_vector.nMax  = weightInfo.nid
    reweight_variables.append(rw_vector)

    # coefficients for the weight parametrization
    param_vector      = TreeVariable.fromString( "p[C/F]" )
    param_vector.nMax = HyperPoly.get_ndof(weightInfo.nvar, options.interpolationOrder)
    hyperPoly         = HyperPoly( options.interpolationOrder )
    reweight_variables.append(param_vector)
    reweight_variables.append(TreeVariable.fromString( "chi2_ndof/F"))

# Write Variables
new_variables  = reweight_variables
new_variables += [ 'weight/F', 'ref_weight/F', 'triggerDecision/I', 'isData/I']
new_variables += [ 'ht/F', 'metSig/F' ]
new_variables += [ 'nJet/I', 'nAllJets/I', 'nBTag/I']
new_variables += [ 'nLep/I', 'nMuon/I', 'nElectron/I', 'nLepTight/I', 'nLepVeto/I']
new_variables += [ 'photonJetdR/F', 'photonLepdR/F' ] 
new_variables += [ 'met_pt_photonEstimated/F', 'met_phi_photonEstimated/F', 'metSig_photonEstimated/F' ]
new_variables += [ 'nPhoton/I' ] 
new_variables += [ 'Jet[%s]'      %nanoJetVarString ]
new_variables += [ 'Electron[%s]' %nanoElectronVarString ]
new_variables += [ 'Muon[%s]'     %nanoMuonVarString ]
new_variables += [ 'Photon[%s]'   %(nanoPhotonVarString + ',photonCat/I') ]
new_variables += [ 'mll/F', 'mllgamma/F' ] 
new_variables += [ 'lldR/F', 'lldPhi/F' ] 
new_variables += [ 'bbdR/F', 'bbdPhi/F' ] 
# Selected BJets
new_variables += [ 'Bj0_' + var for var in nanoBJetVarString.split(',') ]
new_variables += [ 'Bj1_' + var for var in nanoBJetVarString.split(',') ]
# ttgamma categorization

if isMC:
#    nanoGenVarString    += ',photonCat/I'
#    nanoGenJetVarString += ',photonCat/I'
    new_variables += [ 'GenElectron[%s]' %nanoGenVarString ]
    new_variables += [ 'GenMuon[%s]' %nanoGenVarString ]
    new_variables += [ 'GenPhoton[%s]' %nanoGenVarString ]
    new_variables += [ 'GenJet[%s]' %nanoGenJetVarString ]
    new_variables += [ 'GenBJet[%s]' %nanoGenJetVarString ]
    new_variables += [ 'GenTop[%s]' %nanoGenVarString ]
    new_variables += [ 'isTTGamma/I', 'isZGamma/I' ]

if isData:
    new_variables += ['jsonPassed/I']

# Define a reader
reader = sample.treeReader( \
    variables = read_variables ,
    selectionString = "&&".join(skimConds) if not options.sync else "(1)"
    )

# Calculate photonEstimated met
def getMetPhotonEstimated( met_pt, met_phi, photon ):
  met = ROOT.TLorentzVector()
  met.SetPtEtaPhiM(met_pt, 0, met_phi, 0 )
  gamma = ROOT.TLorentzVector()
  gamma.SetPtEtaPhiM(photon['pt'], photon['eta'], photon['phi'], photon['mass'] )
  metGamma = met + gamma
  return (metGamma.Pt(), metGamma.Phi())

def addIndex( collection ):
    for i, col in enumerate(collection):
        col['index'] = i

def get4DVec( part ):
  vec = ROOT.TLorentzVector()
  vec.SetPtEtaPhiM( part['pt'], part['eta'], part['phi'], 0 )
  return vec

def interpret_weight(weight_id):
    str_s = weight_id.split('_')
    res={}
    for i in range(len(str_s)/2):
        res[str_s[2*i]] = float(str_s[2*i+1].replace('m','-').replace('p','.'))
    return res

def fill_vector_collection( event, collection_name, collection_varnames, objects):
    setattr( event, "n"+collection_name, len(objects) )
    for i_obj, obj in enumerate(objects):
        for var in collection_varnames:
            getattr(event, collection_name+"_"+var)[i_obj] = obj[var]

def fill_vector( event, collection_name, collection_varnames, obj):
    for var in collection_varnames:
        setattr(event, collection_name+"_"+var, obj[var] )

def filler( event ):
    # shortcut
    r = reader.event
    if options.sync: sync.print_header( r.run, r.luminosityBlock, r.event )

    event.isData = isData

    if isMC:

        # weight
        event.weight = lumiScaleFactor*r.genWeight if lumiScaleFactor is not None else 0

        # GEN Particles
        gPart = getSortedParticles(r, collVars=nanoGenVars, coll="GenPart")
        # GEN Jets
        gJets = getSortedParticles(r, collVars=nanoGenJetVars, coll="GenJet")

        # Split gen particles
        GenElectron = getGoodParticles( genLeptonSelector(), filterGenElectrons( gPart ) )
        GenMuon     = getGoodParticles( genLeptonSelector(), filterGenMuons( gPart )     )
        GenPhoton   = getGoodParticles( genPhotonSelector(), filterGenPhotons( gPart )   )
        GenTop      = getGoodParticles( genJetSelector(),    filterGenTops( gPart )      )
        GenJet      = getGoodParticles( genJetSelector(),    gJets                       )  
        GenBJet     = getGoodParticles( genJetSelector(),    filterGenBJets( gJets )     )

        # Overlap removal flags for ttgamma/ttbar and Zgamma/DY
        GenIsoPhoton    =      filter( lambda g: isIsolatedPhoton( g, gPart, 0.2 ), GenPhoton )
        event.isTTGamma = len( filter( lambda g: isTTGammaPhoton(  g ),             GenIsoPhoton ) ) > 0 
        event.isZGamma  = len( filter( lambda g: isZGammaPhoton(   g ),             GenIsoPhoton ) ) > 0 

        # Store
        if len(GenElectron) > 0: fill_vector_collection( event, "GenElectron", nanoGenVars,    GenElectron )
        if len(GenMuon) > 0:     fill_vector_collection( event, "GenMuon",     nanoGenVars,    GenMuon )
        if len(GenPhoton) > 0:   fill_vector_collection( event, "GenPhoton",   nanoGenVars,    GenPhoton )
        if len(GenBJet) > 0:     fill_vector_collection( event, "GenBJet",     nanoGenJetVars, GenBJet )
        if len(GenJet) > 0:      fill_vector_collection( event, "GenJet",      nanoGenJetVars, GenJet )
        if len(GenTop) > 0:      fill_vector_collection( event, "GenTop",      nanoGenVars,    GenTop )
        

        # EFT event weights
        if options.addReweights:
            event.nrw    = weightInfo.nid
            lhe_weights  = reader.products['lhe'].weights()
            weights      = []
            param_points = []
            for weight in lhe_weights:
                # Store nominal weight (First position!) 
                if weight.id=='rwgt_1': event.rw_nominal = weight.wgt
                if not weight.id in weightInfo.id: continue
                pos = weightInfo.data[weight.id]
                event.rw_w[pos] = weight.wgt
                weights.append( weight.wgt )
                interpreted_weight = interpret_weight(weight.id)
                for var in weightInfo.variables:
                    getattr( event, "rw_"+var )[pos] = interpreted_weight[var]
                # weight data for interpolation
                if not hyperPoly.initialized:
                    param_points.append( tuple(interpreted_weight[var] for var in weightInfo.variables) )

            # get list of values of ref point in specific order
            ref_point_coordinates = [weightInfo.ref_point_coordinates[var] for var in weightInfo.variables]

            # Initialize with Reference Point
            if not hyperPoly.initialized: hyperPoly.initialize( param_points, ref_point_coordinates )
            coeff = hyperPoly.get_parametrization( weights )

            # = HyperPoly(weight_data, args.interpolationOrder)
            event.np = hyperPoly.ndof
            event.chi2_ndof = hyperPoly.chi2_ndof(coeff, weights)
            #logger.debug( "chi2_ndof %f coeff %r", event.chi2_ndof, coeff )
            if event.chi2_ndof>10**-6: logger.warning( "chi2_ndof is large: %f", event.chi2_ndof )
            for n in xrange(hyperPoly.ndof):
                event.p_C[n] = coeff[n]

            event.ref_weight = event.weight / event.p_C[0]

    elif isData:
        event.weight     = 1.
        event.ref_weight = 1.
        # lumi lists and vetos
        event.jsonPassed  = lumiList.contains(r.run, r.luminosityBlock)
        # make data weight zero if JSON was not passed
        if not event.jsonPassed: event.weight = 0
        # store decision to use after filler has been executed
        event.jsonPassed_ = event.jsonPassed

    else:
        raise NotImplementedError( "isMC %r isData %r " % (isMC, isData) )

    # Leptons
    allLeptons   = getLeptons(r, eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon")
    looseLeptons = getGoodLeptons(r, eleSelector( "loose" ),     muonSelector( "loose" ),     eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon")
    tightLeptons = getGoodLeptons(r, eleSelector( "tight" ),     muonSelector( "tight" ),     eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon")
    vetoLeptons  = getGoodLeptons(r, eleSelector( "thirdVeto" ), muonSelector( "thirdVeto" ), eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon")
    addIndex( looseLeptons )

    looseElectrons  = filter( lambda l:abs(l['pdgId'])==11, looseLeptons)
    looseMuons      = filter( lambda l:abs(l['pdgId'])==13, looseLeptons)

    # Store lepton number
    event.nLep       = len(looseLeptons)
    event.nLepTight  = len(tightLeptons)
    event.nLepVeto   = len(vetoLeptons)         
    event.nElectrons = len(looseElectrons)
    event.nMuons     = len(looseMuons)

    fill_vector_collection( event, "Electron", nanoElectronVars, looseElectrons )
    fill_vector_collection( event, "Muon",     nanoMuonVars,     looseMuons )

    # Jets and lepton jet cross-cleaning.
    allJets  = getSortedParticles(r, collVars=nanoJetVars, coll="Jet")
#    allJets  = getAllJets(r, collVars = nanoJetVars, coll="Jet")
    goodJets = getGoodParticles( jetSelector(), allJets )
#    goodJets = particlePtEtaSelection( allJets, ptCut = 30, absEtaCut = 2.4 )
    goodJets = jetLeptonCleaning( goodJets, looseLeptons, dRCut = 0.4 )
    addIndex( goodJets )

    # Store jets
    event.nJet    = len(goodJets)
    event.nAllJet = len(allJets)

    fill_vector_collection( event, "Jet", nanoJetVars, goodJets )

    # bJets
    bJetsDeepCSV = filterBJets( goodJets, tagger = 'DeepCSV', year = options.year )

    # Store bJets
    bj0, bj1 = ( list(bJetsDeepCSV) + [None, None] )[:2]
    if bj0: fill_vector( event, "Bj0", nanoBJetVars, bj0 )
    if bj1: fill_vector( event, "Bj1", nanoBJetVars, bj1 )

    event.nBTag = len(bJetsDeepCSV)

    # Photons
    allPhotons     = getSortedParticles( r, nanoPhotonVars, coll="Photon" )
    photons        = getGoodParticles( photonSelector( 'loose' ), allPhotons )
#    photons        = getGoodPhotons(r, photon_selector, collVars=nanoPhotonVars, coll="Photon")
    addIndex( photons )

    # Store photons
    if len(photons) > 0:
        # match photon with gen-particle and get its photon category -> reco Photon categorization
        for g in photons:
            genMatch = filter( lambda p: p['index'] == g['genPartIdx'], gPart )[0] if g['genPartIdx'] > 0 and isMC else None
            g['photonCat'] = getPhotonCategory( genMatch, gPart )

        fill_vector_collection( event, "Photon", nanoPhotonVars + ['photonCat'], photons )

        # additional observables
        event.met_pt_photonEstimated, event.met_phi_photonEstimated = getMetPhotonEstimated( r.MET_pt, r.MET_phi, photons[0] )
        if event.ht > 0:          event.metSig_photonEstimated      = event.met_pt_photonEstimated / sqrt( event.ht )
        if len(goodJets) > 0:     event.photonJetdR                 = min( deltaR(photons[0], j ) for j in goodJets )
        if len(looseLeptons) > 0: event.photonLepdR                 = min( deltaR(photons[0], l ) for l in looseLeptons )

    event.nPhoton = len(photons)

    # additional observables
    event.ht         = sum([j['pt'] for j in goodJets])
    event.metSig     = r.MET_pt/sqrt(event.ht) if event.ht>0 else float('nan')

    if len(bJetsDeepCSV) > 1:
        event.bbdR   = deltaR( bJetsDeepCSV[0], bJetsDeepCSV[1] )
        event.bbdPhi = deltaPhi( bJetsDeepCSV[0]['phi'], bJetsDeepCSV[1]['phi'] )

    if len(looseLeptons) > 1:
        event.lldR     = deltaR( looseLeptons[0], looseLeptons[1] )
        event.lldPhi   = deltaPhi( looseLeptons[0]['phi'], looseLeptons[1]['phi'] )
        event.mll      = ( get4DVec(looseLeptons[0]) + get4DVec(looseLeptons[1]) ).M()
        if len(photons) > 0:
            event.mllgamma = ( get4DVec(looseLeptons[0]) + get4DVec(looseLeptons[1]) + get4DVec(photons[0]) ).M()

# Create a maker. Maker class will be compiled. This instance will be used as a parent in the loop
treeMaker_parent = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in new_variables ],
    treeName = "Events"
    )

# Split input in ranges
if options.nJobs>1 and not options.fileBasedSplitting:
    eventRanges = reader.getEventRanges( nJobs = options.nJobs )
else:
    eventRanges = reader.getEventRanges( maxNEvents = options.eventsPerJob, minJobs = options.minNJobs )

logger.info( "Splitting into %i ranges of %i events on average. FileBasedSplitting: %s. Job number %s",  
        len(eventRanges), 
        (eventRanges[-1][1] - eventRanges[0][0])/len(eventRanges), 
        'Yes' if options.fileBasedSplitting else 'No',
        options.job)

#Define all jobs
jobs = [(i, eventRanges[i]) for i in range(len(eventRanges))]

filename, ext = os.path.splitext( os.path.join(output_directory, sample.name + '.root') )

if options.fileBasedSplitting and len(eventRanges)>1:
    raise RuntimeError("Using fileBasedSplitting but have more than one event range!")

clonedEvents = 0
convertedEvents = 0
outputLumiList = {}

for ievtRange, eventRange in enumerate( eventRanges ):

    if not options.fileBasedSplitting and options.nJobs>1:
        if ievtRange != options.job: continue

    logger.info( "Processing range %i/%i from %i to %i which are %i events.",  ievtRange, len(eventRanges), eventRange[0], eventRange[1], eventRange[1]-eventRange[0] )

    # Check whether file exists
    fileNumber = options.job if options.job is not None else 0
    outfilename = filename+'_'+str(fileNumber)+ext
    if os.path.isfile(outfilename):
        logger.info( "Output file %s found.", outfilename)
        if not checkRootFile(outfilename, checkForObjects=["Events"]):
            logger.info( "File %s is broken. Overwriting.", outfilename)
        elif not options.overwrite:
            logger.info( "Skipping.")
            continue
        else:
            logger.info( "Overwriting.")

    tmp_directory = ROOT.gDirectory
    outputfile = ROOT.TFile.Open(outfilename, 'recreate')
    tmp_directory.cd()

    if options.small: 
        logger.info("Running 'small'. Not more than 10000 events") 
        nMaxEvents = eventRange[1]-eventRange[0]
        eventRange = ( eventRange[0], eventRange[0] +  min( [nMaxEvents, 10000] ) )

    # Set the reader to the event range
    reader.setEventRange( eventRange )

    # Clone the empty maker in order to avoid recompilation at every loop iteration
    clonedTree = reader.cloneTree( branchKeepStrings, newTreename = "Events", rootfile = outputfile )
    clonedEvents += clonedTree.GetEntries()
    # Add the TTreeFormulas
    for formula in treeFormulas.keys():
        treeFormulas[formula]['TTreeFormula'] = ROOT.TTreeFormula(formula, treeFormulas[formula]['string'], clonedTree )

    maker = treeMaker_parent.cloneWithoutCompile( externalTree = clonedTree )

    maker.start()
    # Do the thing
    reader.start()

    while reader.run():
        maker.run()
        if isData:
            if maker.event.jsonPassed_:
                if reader.event.run not in outputLumiList.keys():
                    outputLumiList[reader.event.run] = set([reader.event.luminosityBlock])
                else:
                    if reader.event.luminosityBlock not in outputLumiList[reader.event.run]:
                        outputLumiList[reader.event.run].add(reader.event.luminosityBlock)

    convertedEvents += maker.tree.GetEntries()
    maker.tree.Write()
    outputfile.Close()
    logger.info( "Written %s", outfilename)

    # Destroy the TTree
    maker.clear()
    
logger.info( "Converted %i events of %i, cloned %i",  convertedEvents, reader.nEvents , clonedEvents )

# Storing JSON file of processed events
if isData:
    jsonFile = filename+'_%s.json'%(0 if options.nJobs==1 else options.job)
    LumiList( runsAndLumis = outputLumiList ).writeJSON(jsonFile)
    logger.info( "Written JSON file %s",  jsonFile )

logger.info("Copying log file to %s", output_directory )
copyLog = subprocess.call(['cp', logFile, output_directory] )
if copyLog:
    logger.info( "Copying log from %s to %s failed", logFile, output_directory)
else:
    logger.info( "Successfully copied log file" )
    os.remove(logFile)
    logger.info( "Removed temporary log file" )

if writeToDPM:
    for dirname, subdirs, files in os.walk( directory ):
        logger.debug( 'Found directory: %s',  dirname )
        for fname in files:
            source = os.path.abspath(os.path.join(dirname, fname))
            postfix = '_small' if options.small else ''
            cmd = ['xrdcp', source, 'root://hephyse.oeaw.ac.at/%s' % os.path.join( user_dpm_directory, 'postprocessed',  options.processingEra+postfix, options.skim, sample.name, fname ) ]
            logger.info( "Issue copy command: %s", " ".join( cmd ) )
            subprocess.call( cmd )

    # Clean up.
    subprocess.call( [ 'rm', '-rf', directory ] ) # Let's risk it.

