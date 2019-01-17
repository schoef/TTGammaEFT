# Standard Imports
import textwrap

nanoElectronVarString = "deltaEtaSC/F,dr03EcalRecHitSumEt/F,dr03HcalDepth1TowerSumEt/F,dr03TkSumPt/F,dxy/F,dxyErr/F,dz/F,dzErr/F,eInvMinusPInv/F,energyErr/F,eta/F,hoe/F,ip3d/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,sip3d/F,mvaTTH/F,charge/I,cutBased/I,jetIdx/I,pdgId/I,photonIdx/I,tightCharge/I,vidNestedWPBitmap/I,convVeto/O,cutBased_HEEP/O,isPFcand/O,lostHits/b,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoMuonVarString     = "dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,mass/F,dxy/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/I,isPFcand/O,mediumId/O,softId/O,tightId/O,genPartIdx/I,genPartFlav/b,cleanmask/O,isGlobal/O,isTracker/O,pfIsoId/b"
nanoLeptonVarString   = ','.join( set( nanoElectronVarString.split(',') + nanoMuonVarString.split(',') ) )
nanoTauVarString      = "chargedIso/F,dxy/F,dz/F,eta/F,footprintCorr/F,leadTkDeltaEta/F,leadTkDeltaPhi/F,leadTkPtOverTauPt/F,mass/F,neutralIso/F,phi/F,photonsOutsideSignalCone/F,pt/F,puCorr/F,rawAntiEle/F,rawIso/F,rawMVAnewDM/F,rawMVAoldDM/F,rawMVAoldDMdR03/F,charge/I,decayMode/I,jetIdx/I,rawAntiEleCat/F,idAntiEle/I,idAntiMu/I,idDecayMode/I,idDecayModeNewDMs/I,idMVAnewDM/I,idMVAoldDM/I,idMVAoldDMdR03/I,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoPhotonVarString   = "eta/F,energyErr/F,hoe/F,mass/F,mvaID/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,charge/I,cutBased/I,electronIdx/I,jetIdx/I,pdgId/I,vidNestedWPBitmap/I,electronVeto/O,mvaID_WP80/O,mvaID_WP90/O,pixelSeed/O,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoJetVarString      = "area/F,btagCMVA/F,btagCSVV2/F,btagDeepB/F,btagDeepC/F,chEmEF/F,chHEF/F,eta/F,mass/F,neEmEF/F,neHEF/F,phi/F,pt/F,qgl/F,rawFactor/F,electronIdx1/I,electronIdx2/I,jetId/I,muonIdx1/I,muonIdx2/I,nConstituents/I,nElectrons/I,nMuons/I,puId/I,genJetIdx/I,hadronFlavour/I,partonFlavour/I,cleanmask/O"
nanoBJetVarString     = 'pt/F,eta/F,phi/F'
nanoGenVarString      = "eta/F,mass/F,pt/F,phi/F,pdgId/I,genPartIdxMother/I,status/I,statusFlags/I"
nanoGenJetVarString   = "eta/F,mass/F,pt/F,phi/F,partonFlavour/I,hadronFlavour/I"

nanoElectronVars = [item.split('/')[0] for item in nanoElectronVarString.split(',')]
nanoMuonVars     = [item.split('/')[0] for item in nanoMuonVarString.split(',')]
nanoLeptonVars   = [item.split('/')[0] for item in nanoLeptonVarString.split(',')]
nanoTauVars      = [item.split('/')[0] for item in nanoTauVarString.split(',')] 
nanoPhotonVars   = [item.split('/')[0] for item in nanoPhotonVarString.split(',')]
nanoJetVars      = [item.split('/')[0] for item in nanoJetVarString.split(',')]
nanoBJetVars     = [item.split('/')[0] for item in nanoBJetVarString.split(',')]
nanoGenVars      = [item.split('/')[0] for item in nanoGenVarString.split(',')]
nanoGenJetVars   = [item.split('/')[0] for item in nanoGenJetVarString.split(',')]

nanoDataElectronVarString = "deltaEtaSC/F,dr03EcalRecHitSumEt/F,dr03HcalDepth1TowerSumEt/F,dr03TkSumPt/F,dxy/F,dxyErr/F,dz/F,dzErr/F,eInvMinusPInv/F,energyErr/F,eta/F,hoe/F,ip3d/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,sip3d/F,mvaTTH/F,charge/I,cutBased/I,jetIdx/I,pdgId/I,photonIdx/I,tightCharge/I,vidNestedWPBitmap/I,convVeto/O,cutBased_HEEP/O,isPFcand/O,lostHits/b,cleanmask/O"
nanoDataMuonVarString     = "dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,mass/F,dxy/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/I,isPFcand/O,mediumId/O,softId/O,tightId/O,cleanmask/O,isGlobal/O,isTracker/O,pfIsoId/b"
nanoDataLeptonVarString   = ','.join( set( nanoDataElectronVarString.split(',') + nanoDataMuonVarString.split(',') ) )
nanoDataTauVarString      = "chargedIso/F,dxy/F,dz/F,eta/F,footprintCorr/F,leadTkDeltaEta/F,leadTkDeltaPhi/F,leadTkPtOverTauPt/F,mass/F,neutralIso/F,phi/F,photonsOutsideSignalCone/F,pt/F,puCorr/F,rawAntiEle/F,rawIso/F,rawMVAnewDM/F,rawMVAoldDM/F,rawMVAoldDMdR03/F,charge/I,decayMode/I,jetIdx/I,rawAntiEleCat/F,idAntiEle/I,idAntiMu/I,idDecayMode/I,idDecayModeNewDMs/I,idMVAnewDM/I,idMVAoldDM/I,idMVAoldDMdR03/I,cleanmask/O"
nanoDataPhotonVarString   = "eta/F,energyErr/F,hoe/F,mass/F,mvaID/I,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,charge/I,cutBased/I,electronIdx/I,jetIdx/I,pdgId/I,vidNestedWPBitmap/I,electronVeto/O,mvaID_WP80/O,mvaID_WP90/O,pixelSeed/O,cleanmask/O"
nanoDataJetVarString      = "area/F,btagCMVA/F,btagCSVV2/F,btagDeepB/F,btagDeepC/F,chEmEF/F,chHEF/F,eta/F,mass/F,neEmEF/F,neHEF/F,phi/F,pt/F,qgl/F,rawFactor/F,electronIdx1/I,electronIdx2/I,jetId/I,muonIdx1/I,muonIdx2/I,nConstituents/I,nElectrons/I,nMuons/I,puId/I,cleanmask/O"
nanoDataBJetVarString     = 'pt/F,eta/F,phi/F'

nanoDataElectronVars = [item.split('/')[0] for item in nanoDataElectronVarString.split(',')]
nanoDataMuonVars     = [item.split('/')[0] for item in nanoDataMuonVarString.split(',')]
nanoDataLeptonVars   = [item.split('/')[0] for item in nanoDataLeptonVarString.split(',')]
nanoDataTauVars      = [item.split('/')[0] for item in nanoDataTauVarString.split(',')] 
nanoDataPhotonVars   = [item.split('/')[0] for item in nanoDataPhotonVarString.split(',')]
nanoDataJetVars      = [item.split('/')[0] for item in nanoDataJetVarString.split(',')]
nanoDataBJetVars     = [item.split('/')[0] for item in nanoDataBJetVarString.split(',')]

nanoPlotElectronVarString = "eta/F,hoe/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,sieie/F,sip3d/F,cutBased/I,pdgId/I,convVeto/O,lostHits/I,eInvMinusPInv/F"
nanoPlotMuonVarString     = "eta/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,sip3d/F,pdgId/I,mediumId/O,eInvMinusPInv/F"
nanoPlotLeptonVarString   = ','.join( set( nanoPlotElectronVarString.split(',') + nanoPlotMuonVarString.split(',') ) )
nanoPlotTauVarString      = "eta/F,phi/F,pt/F"
nanoPlotPhotonVarString   = "eta/F,hoe/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,sieie/F,cutBased/I,pdgId/I,electronVeto/O,pixelSeed/O"
nanoPlotJetVarString      = "btagCSVV2/F,btagDeepB/F,chEmEF/F,chHEF/F,eta/F,neEmEF/F,neHEF/F,phi/F,pt/F,nConstituents/I,jetId/I"
nanoPlotBJetVarString     = 'pt/F,eta/F,phi/F'

nanoPlotElectronVars = [item.split('/')[0] for item in nanoPlotElectronVarString.split(',')]
nanoPlotMuonVars     = [item.split('/')[0] for item in nanoPlotMuonVarString.split(',')]
nanoPlotLeptonVars   = [item.split('/')[0] for item in nanoPlotLeptonVarString.split(',')]
nanoPlotTauVars      = [item.split('/')[0] for item in nanoPlotTauVarString.split(',')] 
nanoPlotPhotonVars   = [item.split('/')[0] for item in nanoPlotPhotonVarString.split(',')]
nanoPlotJetVars      = [item.split('/')[0] for item in nanoPlotJetVarString.split(',')]
nanoPlotBJetVars     = [item.split('/')[0] for item in nanoPlotBJetVarString.split(',')]

photonIdCutBasedBitmap = {                     'loose':1, 'medium':2, 'tight':4 }  # NanoAOD Version ID bitmap, 2^(0:loose, 1:medium, 2:tight)
photonIdCutBased       = { 'fail':0,           'loose':1, 'medium':2, 'tight':3 }  # NanoAOD Version
electronIdCutBased     = { 'fail':0, 'veto':1, 'loose':2, 'medium':3, 'tight':4 }  # NanoAOD Version

muonPfIsoId            = { 'PFIsoVeryLoose':1, 'PFIsoLoose':2, 'PFIsoMedium':3, 'PFIsoTight':4, 'PFIsoVeryTight':5, 'PFIsoVeryVeryTight':6 }

jetIdNamingList        = [ "tightLepVeto", "tight", "loose" ]

# see https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc80X_doc.html
# or  https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
vidNestedWPBitMapNamingList = [ 'MinPtCut', 'GsfEleSCEtaMultiRangeCut', 'GsfEleDEtaInSeedCut', 'GsfEleDPhiInCut', 'GsfEleFull5x5SigmaIEtaIEtaCut', 'GsfEleHadronicOverEMEnergyScaledCut', 'GsfEleEInverseMinusPInverseCut', 'GsfEleRelPFIsoScaledCut', 'GsfEleConversionVetoCut', 'GsfEleMissingHitsCut' ]
vidNestedWPBitMap           = { 'fail':0, 'veto':1, 'loose':2, 'medium':3, 'tight':4 }  # Bitwise (Electron vidNestedWPBitMap ID flags (3 bits per cut), '000'=0 is fail, '001'=1 is veto, '010'=2 is loose, '011'=3 is medium, '100'=4 is tight)

# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
def jetIdBitMapToDict( val ):
    # convert int of vidNestedWPBitMap ( e.g. val = 6 ) to bitmap ( e.g. "110"), then to list ( e.g. [ 1, 1, 0 ] )
    # Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto : 0 at: 0x5f1a030
    # in 80x no tightLepVeto exists, only 2 bits, bit3 is set to 0
    # create dictionary
    idList = map( lambda x: int(x), "{0:03b}".format( val ) )
    return dict( zip( jetIdNamingList, idList ) )

# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
def vidNestedWPBitMapToDict( val ):
    # convert int of vidNestedWPBitMap ( e.g. val = 611099940 ) to bitmap ( e.g. "100100011011001010010100100100")
    # split vidBitmap string (containing 3 bits per cut) in parts of 3 bits ( e.g. ["100","100","011","011","001","010","010","100","100","100"] )
    # convert 3 bits to int ( e.g. [4, 4, 3, 3, 1, 2, 2, 4, 4, 4])
    # create dictionary
    idList = [ int( x, 2 ) for x in textwrap.wrap( "{0:b}".format( val ) , 3) ] #use 2 for nanoAOD version 80x
    return dict( zip( vidNestedWPBitMapNamingList, idList ) )

# General Selection Functions
def particlePtEtaSelection( collection, ptCut=10, absEtaCut=2.4 ):
    parts = list( filter( lambda p: p['pt'] > ptCut and abs(p['eta']) < absEtaCut, collection ) )
    parts.sort( key = lambda l: -l['pt'] )
    return parts

def deltaRCleaning( cleaningParticles, otherParticles, dRCut = 0.4 ):

    from TTGammaEFT.Tools.observables   import deltaR

    res = []
    for part in cleaningParticles:
        clean = True
        for otherParticle in otherParticles:
            if deltaR( otherParticle, part ) < dRCut:
                clean = False
                break
        if clean:
            res.append( part )
    res.sort( key = lambda p: -p['pt'] )
    return res

def getUnsortedParticles( c, collVars, coll ):
    from TTGammaEFT.Tools.helpers import getVarValue, getObjDict
    return [ getObjDict( c, coll+'_', collVars, i ) for i in range(int(getVarValue(c, 'n'+coll))) ]

def getSortedParticles( c, collVars, coll ):
    part = getUnsortedParticles( c, collVars, coll )
    part.sort( key = lambda l: -l['pt'] )
    return part

def getGoodParticles( selector, coll ):
    part = list( filter( lambda l: selector(l), coll ) )
    part.sort( key = lambda l: -l['pt'] )
    return part
    
def isGoodParticle( p, ptCut=10, absEtaCut=2.4 ):
    return p['pt'] > ptCut and abs(p['eta']) < absEtaCut

# Reco Leptons
def getLeptons(c, eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon"):
    leptons  = getUnsortedParticles( c, eleCollVars,  eleColl  )
    leptons += getUnsortedParticles( c, muonCollVars, muonColl )
    leptons.sort( key = lambda l:-l['pt'] )
    return leptons

def getGoodLeptons(c, eleSelector, muonSelector, eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon"):
    leptons  = getGoodParticles( eleSelector,  getUnsortedParticles( c, eleCollVars,  eleColl  ) )
    leptons += getGoodParticles( muonSelector, getUnsortedParticles( c, muonCollVars, muonColl ) )
    leptons.sort( key = lambda l:-l['pt'] )
    return leptons

# Reco b-Jet Filter
def isBJet( j, tagger='DeepCSV', year=2016 ):
    if tagger == 'CSVv2':
        if year == 2016:
            # https://twiki.cern.ch/twikix/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagCSVV2'] > 0.8484 
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagCSVV2'] > 0.8838 
        elif year == 2018:
            # UPDATE WHEN AVAILABLE
            return j['btagCSVV2'] > 0.8838 
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)
    elif tagger == 'DeepCSV':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation2016Legacy
            return j['btagDeepB'] > 0.6321
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagDeepB'] > 0.4941
        elif year == 2018:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
            return j['btagDeepB'] > 0.4184
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def filterBJets( jets, tagger='DeepCSV', year=2016 ):
    bJets = list( filter( lambda j: isBJet(j, tagger=tagger, year=year), jets ) )
    bJets.sort( key=lambda j: -j['pt'] )
    return bJets

def filterNonBJets( jets, tagger='DeepCSV', year=2016 ):
    nonBJets = list( filter( lambda j: not isBJet(j, tagger=tagger, year=year), jets ) )
    nonBJets.sort( key=lambda j: -j['pt'] )
    return nonBJets

def vertexSelector( l ):
#    if abs(l['pdgId']) == 11: absEta = abs(l["eta"] + l["deltaEtaSC"])   # eta supercluster
#    else:                     absEta = abs(l["eta"])                     # eta
    EC = 0 #absEta > 1.479 # only if difference for EndCaps
    if abs(l["dxy"]) >= 0.05 + 0.05*EC: return False
    if abs(l["dz"])  >= 0.1 + 0.1*EC:  return False
    return True

def photonMediumIDSelector( p, year, removedCuts=[], printVar=False ):
    # https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedPhotonIdentificationRun2

    if year not in [ 2016, 2017, 2018 ]:
        raise ( NotImplementedError, "Don't know what cut to use for year %s"%year )

    missingCuts = list( set( removedCuts ) - set( [ "hoe", "sieie", "pfRelIso03_chg", "pfRelIso03_all", "pfRelIso03_n" ] ) )
    if len( missingCuts ):
        raise ( NotImplementedError, "Cuts %s not in medium photon cutbased ID"%", ".join( missingCuts ))

    EC                 = abs(p["eta"]) > 1.479
    pfRelIso03_neutral = p["pfRelIso03_all"] - p["pfRelIso03_chg"]

    if EC and year == 2016: # photon medium cutbased ID 2016 EC
        hoe_cut                = 0.0219
        sieie_cut              = 0.03001
        pfRelIso03_chg_cut     = 0.442
        pfRelIso03_neutral_cut = 1.715 + 0.0163 * p["pt"] + 0.000014 * p["pt"] * p["pt"]
        pfRelIso03_all_cut     = 3.863 + 0.0034 * p["pt"]
    elif not EC and year == 2016: # photon medium cutbased ID 2016 Barrel
        hoe_cut                = 0.0396
        sieie_cut              = 0.01022
        pfRelIso03_chg_cut     = 0.441
        pfRelIso03_neutral_cut = 2.725 + 0.0148 * p["pt"] + 0.000017 * p["pt"] * p["pt"] 
        pfRelIso03_all_cut     = 2.571 + 0.0047 * p["pt"]
    elif EC and year != 2016: # photon medium cutbased ID 2017 EC
        hoe_cut                = 0.0326
        sieie_cut              = 0.0272
        pfRelIso03_chg_cut     = 1.051
        pfRelIso03_neutral_cut = 2.718 + 0.0117 * p["pt"] + 0.000023 * p["pt"] * p["pt"]
        pfRelIso03_all_cut     = 3.867 + 0.0037 * p["pt"]
    elif not EC and year != 2016: # photon medium cutbased ID 2017 Barrel
        hoe_cut                = 0.02197
        sieie_cut              = 0.01015
        pfRelIso03_chg_cut     = 1.141
        pfRelIso03_neutral_cut = 1.189 + 0.01512  * p["pt"] + 0.00002259 * p["pt"] * p["pt"]
        pfRelIso03_all_cut     = 2.08  + 0.004017 * p["pt"]

    if ("sieie"          not in removedCuts) and (p["sieie"]            >= sieie_cut):#              return False
                if printVar: print "sieie"
                return False
    if ("pfRelIso03_chg" not in removedCuts) and (p["pfRelIso03_chg"]   >= pfRelIso03_chg_cut):#     return False
                if printVar: print "pfRelIso03_chg"
                return False
    if ("pfRelIso03_all" not in removedCuts) and (p["pfRelIso03_all"]   >= pfRelIso03_all_cut):#     return False
                if printVar: print "pfRelIso03_all"
                return False
    if ("pfRelIso03_n"   not in removedCuts) and (pfRelIso03_neutral    >= pfRelIso03_neutral_cut):# return False
                if printVar: print "pfRelIso03_n"
                return False
    if ("hoe"            not in removedCuts) and (p["hoe"]              >= hoe_cut):
                if printVar: print "hoe"
                return False
    return True

# nanoAOD 94x or higher
def triggerEmulatorSelector( l, wp ):
    cutDict    = vidNestedWPBitMapToDict( l['vidNestedWPBitmap'] )
    wpCutValue = vidNestedWPBitMap[ wp ]     
    return all( val >= wpCutValue for val in cutDict.values() )

#def triggerEmulatorSelector( l, wp ):
#    # still missing: dPhiSC, dEtaSC (switch to triggerEmulatorCuts in nanoAOD 94x or higher)
#    ECSc = abs(l["eta"] + l["deltaEtaSC"]) > 1.479
#    if l["sieie"]            >= (0.011+0.019*ECSc): return False
#    if l["eInvMinusPInv"]    <= -0.05:              return False
#    if l["eInvMinusPInv"]    >= (0.01-0.005*ECSc):  return False
#    if l["hoe"]              >= (0.10-0.03*ECSc):   return False
#    return True

def barrelEndcapVeto( p ):
    if abs(p['pdgId']) == 11: absEta = abs(p["eta"] + p["deltaEtaSC"])   # eta supercluster
    else:                     absEta = abs(p["eta"])                     # eta
    return ( absEta > 1.556 or absEta <= 1.4442 )

# Reco Selectors
def jetSelector( year, noPtEtaCut=False ):
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetIDhttps://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID
    if year == 2016:
        # According to AN-2017/197
        # jetID cuts, pT and eta cuts
        def func(j):
            if not noPtEtaCut:
                if j["pt"]       <= 30:                      return False
                if abs(j["eta"]) >= 2.4:                     return False
            if not jetIdBitMapToDict( j["jetId"] )["loose"]: return False
            return True
        return func

    elif year == 2017 or year == 2018:
        # jetID cuts, pT and eta cuts
        def func(j):
            if not noPtEtaCut:
                if j["pt"]       <= 30:                      return False
                if abs(j["eta"]) >= 2.4:                     return False
            if not jetIdBitMapToDict( j["jetId"] )["tight"]: return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def muonSelector( lepton_selection, leading=False, noPtEtaCut=False ):
    # According to AN-2017/197
    if lepton_selection == 'tight':
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <  30:                         return False
                if abs(l["eta"])   >= 2.4:                        return False
            if not l["tightId"]:                                  return False
            if not vertexSelector(l):                             return False
            if l['pfRelIso03_all'] >= 0.12:                       return False
#            if l['pfIsoId']        <  muonPfIsoId['PFIsoMedium']: return False
            if l["sip3d"]          >= 4:                          return False
            return True
        return func

    elif lepton_selection == 'medium':
        ptCut = 25 if leading else 15
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <= ptCut:                      return False
                if abs(l["eta"])   >= 2.4:                        return False
            if not l["mediumId"]:                                 return False
            if not vertexSelector(l):                             return False
            if l['pfRelIso03_all'] >= 0.12:                       return False
#            if l['pfIsoId']        <  muonPfIsoId['PFIsoMedium']: return False
            if l["sip3d"]          >= 4:                          return False
            return True
        return func

    elif lepton_selection == 'veto':
        # muon loose requirement
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <= 15:                            return False
                if abs(l["eta"])   >= 2.4:                           return False
            if not l["isPFcand"]:                                    return False
            if not ( l["isGlobal"] or l["isTracker"] ):              return False
            if not vertexSelector(l):                                return False
            if l['pfRelIso03_all'] >= 0.4:                           return False
#            if l['pfIsoId']        <  muonPfIsoId['PFIsoVeryLoose']: return False
            if l["sip3d"]          >= 4:                             return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for muons")

# electrons 
def eleSelector( lepton_selection, leading=False, noPtEtaCut=False ):
    idVar = "cutBased"
    # According to AN-2017/197
    if lepton_selection == 'tight':
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <  35:                return False
                if abs(l["eta"])   >= 2.1:               return False
            if not barrelEndcapVeto(l):                  return False
            if l[idVar] < electronIdCutBased['tight']:   return False
            if l['pfRelIso03_all'] >= 0.12:              return False
            if l["sip3d"]          >= 4:                 return False
            if int(l["lostHits"])  != 0:                 return False
            if not l["convVeto"]:                        return False
            if not vertexSelector(l):                    return False
#            if not triggerEmulatorSelector(l, 'medium'): return False # only when not using cutBasedId
            return True
        return func

    elif lepton_selection == 'medium':
        ptCut = 25 if leading else 15
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <= ptCut:             return False
                if abs(l["eta"])   >= 2.4:               return False
            if not barrelEndcapVeto(l):                  return False
            if l[idVar] < electronIdCutBased['medium']:  return False
            if l['pfRelIso03_all'] >= 0.12:              return False
            if l["sip3d"]          >= 4:                 return False
            if int(l["lostHits"])  != 0:                 return False
            if not l["convVeto"]:                        return False
            if not vertexSelector(l):                    return False
#            if not triggerEmulatorSelector(l, 'medium'): return False # only when not using cutBasedId
            return True
        return func

    elif lepton_selection == 'veto':
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <= 15:              return False
                if abs(l["eta"])   >= 2.4:             return False
            if not barrelEndcapVeto(l):                return False
            if l[idVar] < electronIdCutBased['veto']:  return False
            if l['pfRelIso03_all'] >= 0.4:             return False
            if l["sip3d"]          >= 4:               return False
            if not vertexSelector(l):                  return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for electrons")

def tauSelector( lepton_selection ):
    # dummy function
        def func(l):
            return True
        return func

def photonSelector( selection, noPtEtaCut=False, year=None, removedCuts=[] ):
    # According to AN-2017/197
    idVar    = "cutBased"       if year==2016 else "cutBasedBitmap"
    photonId = photonIdCutBased if year==2016 else photonIdCutBasedBitmap

    if selection == "medium":
        def func(g):
            if not noPtEtaCut:
                if g["pt"]       <= 20:                                             return False
                if abs(g["eta"]) >= 1.479:                                          return False # Barrel only
#            if g[idVar]          <  photonId[selection]:                            return False # seems to be a problem with hoe cut
            if not photonMediumIDSelector( g, year=year, removedCuts=removedCuts ): return False
            if g["pixelSeed"]:                                                      return False
            if not g["electronVeto"]:                                               return False
            return True
        return func

    elif selection == "loose":
        def func(g):
            if not noPtEtaCut:
                if g["pt"]       <= 20:                                             return False
                if abs(g["eta"]) >= 1.479:                                          return False # Barrel only
            if g[idVar]          <  photonId[selection]:                            return False
            if g["pixelSeed"]:                                                      return False
            if not g["electronVeto"]:                                               return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for photons")


# Gen Selectors
def genJetSelector():
    # According to AN-2017/197
    def func(j):
        if j["pt"]       <= 30:  return False
        if abs(j["eta"]) >= 2.4: return False
        return True
    return func

def genLeptonSelector():
    # According to AN-2017/197
    def func(l):
        if l["pt"]       <= 15:  return False
        if abs(l["eta"]) >= 2.4: return False
        return True
    return func

def genPhotonSelector( photon_selection=None ):
    # According to AN-2017/197
    if photon_selection == 'overlapTTGamma':
        # Remove events from ttbar sample, keep ttgamma events
        def func(g):
            if g["pt"]       <= 13:  return False
            if abs(g["eta"]) >= 3.0: return False
            return True
        return func

    elif photon_selection == 'overlapZWGamma':
        # Remove events from DY and W+jets sample, keep Zgamma and Wgamma events
        def func(g):
            if g["pt"]       <= 15:  return False
            if abs(g["eta"]) >= 2.6: return False
            return True
        return func

    elif photon_selection == 'overlapSingleTopTch':
        # Remove events from single top t-channel sample, keep single top + photon events
        def func(g):
            if g["pt"]       <= 10:  return False
            if abs(g["eta"]) >= 2.6: return False
            return True
        return func

    else:
        # general gen-photon selection
        def func(g):
            if g["pt"]       <= 13:    return False
            if abs(g["eta"]) >= 1.479: return False
            return True
        return func

# Gen Particle Filter
def filterGenElectrons( genParts, status=None ):
    if   status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
    else:                   stat = [1,23]
    electrons = list( filter( lambda l: abs(l['pdgId']) == 11 and l['status'] in stat, genParts ) )
    electrons.sort( key = lambda l:-l['pt'] )
    return electrons

def filterGenMuons( genParts, status=None ):
    if   status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
    else:                   stat = [1,23]
    muons = list( filter( lambda l: abs(l['pdgId']) == 13 and l['status'] in stat, genParts ) )
    muons.sort( key = lambda l:-l['pt'] )
    return muons

def filterGenPhotons( genParts, status=None ):
    if   status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
    else:                   stat = [1,23]
    photons = list( filter( lambda l: abs(l['pdgId']) == 22 and l['status'] in stat, genParts ) )
    photons.sort( key = lambda l:-l['pt'] )
    return photons

def filterGenTops( genParts ):
    tops = list( filter( lambda l: abs(l['pdgId']) == 6 and l['status'] == 62, genParts ) )
    tops.sort( key = lambda l:-l['pt'] )
    return tops

def filterGenBJets( genJets ):
    bjets = list( filter( lambda j: abs(j['hadronFlavour']) == 5, genJets ) )
    bjets.sort( key = lambda j:-j['pt'] )
    return bjets

# Pythia status flags:
# 62: outgoing subprocess particle with primordial kT included, last gencopy before it decays
# 23: outgoing
# 71: copied partons to collect into contiguous colour singlet (jets)
#  1: stage of event generation inside PYTHIA
# 22: intermediate (intended to have preserved mass) (tops)
