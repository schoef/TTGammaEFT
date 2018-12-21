# Standard Imports
import textwrap

nanoElectronVarString = "deltaEtaSC/F,dr03EcalRecHitSumEt/F,dr03HcalDepth1TowerSumEt/F,dr03TkSumPt/F,dxy/F,dxyErr/F,dz/F,dzErr/F,eInvMinusPInv/F,energyErr/F,eta/F,hoe/F,ip3d/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,sip3d/F,mvaTTH/F,charge/I,cutBased/I,jetIdx/I,pdgId/I,photonIdx/I,tightCharge/I,vidNestedWPBitmap/I,convVeto/O,cutBased_HEEP/O,isPFcand/O,lostHits/b,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoMuonVarString     = "dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,mass/F,dxy/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/I,isPFcand/O,mediumId/O,softId/O,tightId/O,genPartIdx/I,genPartFlav/b,cleanmask/O" #,isGlobal/O
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
nanoDataMuonVarString     = "dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,mass/F,dxy/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/I,isPFcand/O,mediumId/O,softId/O,tightId/O,cleanmask/O" #,isGlobal/O
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
jetIdBitwise           = { 'fail':0,           'loose':1,             'tight':3 }  # Bitwise (Jet ID flags bit1 is loose, bit2 is tight -> int(00)=0 == fail, int(01)=1 == loose, int(11)=3 == tight)

# see https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc80X_doc.html
# or  https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
vidNestedWPBitMapNamingList = [ 'MinPtCut', 'GsfEleSCEtaMultiRangeCut', 'GsfEleDEtaInSeedCut', 'GsfEleDPhiInCut', 'GsfEleFull5x5SigmaIEtaIEtaCut', 'GsfEleHadronicOverEMEnergyScaledCut', 'GsfEleEInverseMinusPInverseCut', 'GsfEleRelPFIsoScaledCut', 'GsfEleConversionVetoCut', 'GsfEleMissingHitsCut' ]
vidNestedWPBitMap           = { 'fail':0, 'veto':1, 'loose':2, 'medium':3, 'tight':4 }  # Bitwise (Electron vidNestedWPBitMap ID flags (3 bits per cut), '000'=0 is fail, '001'=1 is veto, '010'=2 is loose, '011'=3 is medium, '100'=3 is tight)

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
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagDeepB'] > 0.6324
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagDeepB'] > 0.4941
        elif year == 2018:
            # UPDATE WHEN AVAILABLE
            return j['btagDeepB'] > 0.4941
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def filterBJets( jets, tagger='DeepCSV', year=2016 ):
    bJets = list( filter( lambda j: isBJet(j, tagger = tagger, year = year), jets ) )
    bJets.sort( key = lambda j: -j['pt'] )
    return bJets

def filterNonBJets( jets, tagger='DeepCSV', year=2016 ):
    nonBJets = list( filter( lambda j: not isBJet(j, tagger = tagger, year = year), jets ) )
    nonBJets.sort( key = lambda j: -j['pt'] )
    return nonBJets

def vertexSelector( l ):
    if abs(l["dxy"]) >= 0.05: return False
    if abs(l["dz"])  >= 0.1:  return False
    return True

def photonIDSelector( p ):
    # ( should be medium cutbased ID, however is not!?! )
    EC                 = abs(p["eta"]) > 1.479
#    pfRelIso03_neutral = p["pfRelIso03_all"] - p["pfRelIso03_chg"]
#    pT                 = p["pt"]
#    pT2                = pT*pT

#    if EC:
#        pfRelIso03_all_cut     = 2.571 + 0.0047*pT
#        pfRelIso03_neutral_cut = 1.715 + 0.0163*pT + 0.000014*pT2
#    else:
#        pfRelIso03_all_cut     = 3.863 + 0.0034*pT
#        pfRelIso03_neutral_cut = 2.725 + 0.0148*pT + 0.000017*pT2 

    if p["hoe"]              >= (0.0396-0.0177*EC):     return False
    if p["sieie"]            >= (0.01022+0.01979*EC):   return False
    if p["pfRelIso03_chg"]   >= (0.441+0.001*EC):       return False
#    if p["pfRelIso03_all"]   >= pfRelIso03_all_cut:     return False
#    if pfRelIso03_neutral    >= pfRelIso03_neutral_cut: return False
    return True

# nanoAOD 94x or higher
def triggerEmulatorCuts( l, wp ):
    cutDict    = vidNestedWPBitMapToDict( l['vidNestedWPBitmap'] )
    wpCutValue = vidNestedWPBitMap[ wp ]     
    return all( val >= wpCutValue for val in cutDict.values() )

def triggerEmulatorSelector( l ):
    # still missing: dPhiSC, dEtaSC (switch to triggerEmulatorCuts in nanoAOD 94x or higher)
    ECSc = abs(l["eta"] + l["deltaEtaSC"]) > 1.479
    if l["sieie"]            >= (0.011+0.019*ECSc): return False
    if l["eInvMinusPInv"]    <= -0.05:              return False
    if l["eInvMinusPInv"]    >= (0.01-0.005*ECSc):  return False
    if l["hoe"]              >= (0.10-0.03*ECSc):   return False
    return True

def barrelEndcapVeto( p ):
    if abs(p['pdgId']) == 11: absEta = abs(p["eta"] + p["deltaEtaSC"])   # eta supercluster
    else:                     absEta = abs(p["eta"])                     # eta
    return ( absEta > 1.556 or absEta <= 1.4442 )

# Reco Selectors
def jetSelector( jet_selection ):
    # According to AN-2017/197
    if jet_selection == 'loose':
        def func(j):
            if j["pt"]            <= 30:           return False
            if abs(j["eta"])      >= 2.4:          return False
            if j["nConstituents"]  < 2:            return False
            if j["neHEF"]         >= 0.99:         return False
            if j["neEmEF"]        >= 0.99:         return False
            if j["chEmEF"]        >= 0.99:         return False
            if j["chHEF"]         <= 0.:           return False
            if j["jetId"] < jetIdBitwise['loose']: return False
            return True
        return func
    elif jet_selection == 'basic':
        def func(j):
            if j["pt"]            <= 30:           return False
            if abs(j["eta"])      >= 2.4:          return False
            return True
        return func

def muonSelector( lepton_selection ):
    # According to AN-2017/197
    # muon veto: isGlobal still missing (in nanoAOD 94x or higher)
    if lepton_selection == 'tight':
        def func(l):
            if l["pt"]             <= 25:   return False
            if abs(l["eta"])       >= 2.4:  return False
            if l['pfRelIso03_all'] >= 0.12: return False
            if l["sip3d"]          >= 4:    return False
            if not vertexSelector(l):       return False
            if not l["mediumId"]:           return False
            return True
        return func

    elif lepton_selection == 'loose':
        def func(l):
            if l["pt"]             <= 15:   return False
            if abs(l["eta"])       >= 2.4:  return False
            if l['pfRelIso03_all'] >= 0.12: return False
            if l["sip3d"]          >= 4:    return False
            if not vertexSelector(l):       return False
            if not l["mediumId"]:           return False
            return True
        return func

    elif lepton_selection == 'veto':
        def func(l):
            if l["pt"]             <= 15:   return False
            if abs(l["eta"])       >= 2.4:  return False
            if l['pfRelIso03_all'] >= 0.4:  return False
            if l["sip3d"]          >= 4:    return False
            if not vertexSelector(l):       return False
#            if not l["isGlobal"]:           return False
            return True
        return func

    elif lepton_selection == 'basic':
        def func(l):
            if l["pt"]             <= 15:   return False
            if abs(l["eta"])       >= 2.4:  return False
            return True
        return func

# electrons 
def eleSelector( lepton_selection ):
    # According to AN-2017/197
    # still missing: MVA
    idVar = "cutBased"
    if lepton_selection == 'tight':
        def func(l):
            if l["pt"]             <= 25:              return False
            if abs(l["eta"])       >= 2.4:             return False
            if not barrelEndcapVeto(l):                return False
            if l['pfRelIso03_all'] >= 0.12:            return False
            if l["sip3d"]          >= 4:               return False
            if int(l["lostHits"])  != 0:               return False
            if not l["convVeto"]:                      return False
            if not vertexSelector(l):                  return False
            if not triggerEmulatorSelector(l):         return False
#            if not triggerEmulatorCuts(l, 'medium'):   return False
            if l[idVar] < electronIdCutBased['medium']: return False
            return True
        return func

    elif lepton_selection == 'loose':
        def func(l):
            if l["pt"]             <= 15:              return False
            if abs(l["eta"])       >= 2.4:             return False
            if not barrelEndcapVeto(l):                return False
            if l['pfRelIso03_all'] >= 0.12:            return False
            if l["sip3d"]          >= 4:               return False
            if int(l["lostHits"])  != 0:               return False
            if not l["convVeto"]:                      return False
            if not vertexSelector(l):                  return False
            if not triggerEmulatorSelector(l):         return False
#            if not triggerEmulatorCuts(l, 'medium'):   return False
            if l[idVar] < electronIdCutBased['medium']: return False
            return True
        return func

    elif lepton_selection == 'veto':
        def func(l):
            if l["pt"]             <= 15:              return False
            if abs(l["eta"])       >= 2.4:             return False
            if not barrelEndcapVeto(l):                return False
            if l['pfRelIso03_all'] >= 0.4:             return False
            if l["sip3d"]          >= 4:               return False
            if not vertexSelector(l):                  return False
            if l[idVar] < electronIdCutBased['veto']:  return False
            return True
        return func

    elif lepton_selection == 'basic':
        def func(l):
            if l["pt"]             <= 15:              return False
            if abs(l["eta"])       >= 2.4:             return False
            return True
        return func

def tauSelector( lepton_selection ):
    # dummy function
        def func(l):
            return True
        return func

def photonSelector( selection, year=2016 ):
    # According to AN-2017/197
    idVar    = "cutBased"       if year==2016 else "cutBasedBitmap"
    photonId = photonIdCutBased if year==2016 else photonIdCutBasedBitmap
    if selection == 'medium':
        def func(g):
            if g["pt"]       <= 20:           return False
            if abs(g["eta"]) >= 1.479:        return False
            if g["pixelSeed"]:                return False
            if not barrelEndcapVeto(g):       return False
            if not photonIDSelector(g):       return False
            if not g["electronVeto"]:         return False
            if g[idVar] < photonId['medium']: return False
            return True
        return func

    elif selection == 'basic':
        def func(g):
            if g["pt"]       <= 13:           return False
            if abs(g["eta"]) >= 1.479:        return False
            return True
        return func

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

def genPhotonSelector( photon_selection = None ):
    # According to AN-2017/197
    if photon_selection == 'overlapTTGamma':
        def func(g):
            if g["pt"]       <= 13:  return False
            if abs(g["eta"]) >= 3.0: return False
            return True
        return func

    if photon_selection == 'overlapZGamma':
        def func(g):
            if g["pt"]       <= 15:  return False
            if abs(g["eta"]) >= 2.6: return False
            return True
        return func

    if photon_selection == 'overlapSingleT':
        # To Do
        def func(g):
            return True
        return func

    if photon_selection is None:
        def func(g):
            if g["pt"]       <= 13:    return False
            if abs(g["eta"]) >= 1.479: return False
            return True
        return func

# Gen Particle Filter
def filterGenElectrons( genParts, status=None ):
    if status is None:      stat = [1,23]
    elif status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
    electrons = list( filter( lambda l: abs(l['pdgId']) == 11 and l['status'] in stat, genParts ) )
    electrons.sort( key = lambda l:-l['pt'] )
    return electrons

def filterGenMuons( genParts, status=None ):
    if status is None:      stat = [1,23]
    elif status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
    muons = list( filter( lambda l: abs(l['pdgId']) == 13 and l['status'] in stat, genParts ) )
    muons.sort( key = lambda l:-l['pt'] )
    return muons

def filterGenPhotons( genParts, status=None ):
    if status is None:      stat = [1,23]
    elif status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
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

def getFilterCut( isData=False, isFastSim=False, year=2016, ignoreJSON=False ):
    if isFastSim:
        filters             = [ "Flag_goodVertices" ]
    elif year == 2016:
        filters             = [ "Flag_goodVertices" ]
        filters            += [ "Flag_HBHENoiseFilter" ]
        filters            += [ "Flag_HBHENoiseIsoFilter" ]
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]
#        filters            += [ "Flag_BadPFMuonFilter" ]
#        filters            += [ "Flag_BadChargedCandidateFilter" ]
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]
    elif year == 2017:
        filters             = [ "Flag_goodVertices" ]
        filters            += [ "Flag_HBHENoiseFilter" ]
        filters            += [ "Flag_HBHENoiseIsoFilter" ]
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]
        filters            += [ "Flag_BadPFMuonFilter" ]
        filters            += [ "Flag_BadChargedCandidateFilter" ]
#        filters            += [ "ecalBadCalibReducedMINIAODFilter" ]
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]
    if isData:
        filters            += [ "weight>0" ]
        if not ignoreJSON:
            filters        += [ "jsonPassed>0" ]
    return "&&".join(filters)


# switch to that in next pp
def getFilterCutsAll( year, isData=False, ignoreJSON=False ):
    # Flag_ecalBadCalibReducedMINIAODFilter not yet implemented
    # Flag_BadPFMuonFilter and Flag_BadChargedCandidateFilter in version 94x or higher

    if year == 2016:
        filters             = [ "Flag_goodVertices" ]                         # primary vertex filter
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]       # beam halo filter
        filters            += [ "Flag_HBHENoiseFilter" ]                      # HBHE noise filter
        filters            += [ "Flag_HBHENoiseIsoFilter" ]                   # HBHEiso noise filter
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]   # ECAL TP filter
#        filters            += [ "Flag_BadPFMuonFilter" ]                      # Bad PF Muon Filter (re-run nanoAOD processing)
#        filters            += [ "Flag_BadChargedCandidateFilter" ]            # Bad Charged Hadron Filter (re-run nanoAOD processing)
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]                        # ee badSC noise filter (data only)

    elif year == 2017:
        filters             = [ "Flag_goodVertices" ]                         # primary vertex filter
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]       # beam halo filter
        filters            += [ "Flag_HBHENoiseFilter" ]                      # HBHE noise filter
        filters            += [ "Flag_HBHENoiseIsoFilter" ]                   # HBHEiso noise filter
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]   # ECAL TP filter
        filters            += [ "Flag_BadPFMuonFilter" ]                      # Bad PF Muon Filter
        filters            += [ "Flag_BadChargedCandidateFilter" ]            # Bad Charged Hadron Filter
#        filters            += [ "Flag_ecalBadCalibReducedMINIAODFilter" ]     # ECAL bad calibration filter update (needs to be re-run on miniAOD)
        filters            += [ "Flag_ecalBadCalibFilter" ]                   # current replacement for Flag_ecalBadCalibReducedMINIAODFilter
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]                        # ee badSC noise filter (data only)

    elif year == 2018:
        filters             = [ "Flag_goodVertices" ]                         # primary vertex filter
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]       # beam halo filter
        filters            += [ "Flag_HBHENoiseFilter" ]                      # HBHE noise filter
        filters            += [ "Flag_HBHENoiseIsoFilter" ]                   # HBHEiso noise filter
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]   # ECAL TP filter
        filters            += [ "Flag_BadPFMuonFilter" ]                      # Bad PF Muon Filter
        filters            += [ "Flag_BadChargedCandidateFilter" ]            # Bad Charged Hadron Filter
#        filters            += [ "Flag_ecalBadCalibReducedMINIAODFilter" ]     # ECAL bad calibration filter update (needs to be re-run on miniAOD)
        filters            += [ "Flag_ecalBadCalibFilter" ]                   # current replacement for Flag_ecalBadCalibReducedMINIAODFilter
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]                        # ee badSC noise filter (data only)

    else:
        raise NotImplementedError( "No MET filter found for year %i" %year )

    if isData:
        filters            += [ "weight>0" ]
        if not ignoreJSON:
            filters        += [ "jsonPassed>0" ]

    return "&&".join(filters)

