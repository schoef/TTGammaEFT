nanoElectronVarString = "deltaEtaSC/F,dr03EcalRecHitSumEt/F,dr03HcalDepth1TowerSumEt/F,dr03TkSumPt/F,dxy/F,dxyErr/F,dz/F,dzErr/F,eCorr/F,eInvMinusPInv/F,energyErr/F,eta/F,hoe/F,ip3d/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,sip3d/F,mvaTTH/F,charge/I,cutBased/I,jetIdx/I,pdgId/I,photonIdx/I,tightCharge/I,vidNestedWPBitmap/I,convVeto/O,cutBased_HEEP/O,isPFcand/O,lostHits/b,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoMuonVarString     = "dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,mass/F,dxy/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/I,isPFcand/O,mediumId/O,softId/O,tightId/O,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoLeptonVarString   = ','.join( set( nanoElectronVarString.split(',') + nanoMuonVarString.split(',') ) )
nanoTauVarString      = "chargedIso/F,dxy/F,dz/F,eta/F,footprintCorr/F,leadTkDeltaEta/F,leadTkDeltaPhi/F,leadTkPtOverTauPt/F,mass/F,neutralIso/F,phi/F,photonsOutsideSignalCone/F,pt/F,puCorr/F,rawAntiEle/F,rawIso/F,rawMVAnewDM/F,rawMVAoldDM/F,rawMVAoldDMdR03/F,charge/I,decayMode/I,jetIdx/I,rawAntiEleCat/F,idAntiEle/I,idAntiMu/I,idDecayMode/I,idDecayModeNewDMs/I,idMVAnewDM/I,idMVAoldDM/I,idMVAoldDMdR03/I,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoPhotonVarString   = "eta/F,eCorr/F,energyErr/F,hoe/F,mass/F,mvaID/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,charge/I,cutBased/I,electronIdx/I,jetIdx/I,pdgId/I,vidNestedWPBitmap/I,electronVeto/O,mvaID_WP80/O,mvaID_WP90/O,pixelSeed/O,genPartIdx/I,genPartFlav/b,cleanmask/O"
nanoJetVarString      = "area/F,btagCMVA/F,btagCSVV2/F,btagDeepB/F,btagDeepC/F,chEmEF/F,chHEF/F,eta/F,mass/F,neEmEF/F,neHEF/F,phi/F,pt/F,qgl/F,rawFactor/F,bReg/F,electronIdx1/I,electronIdx2/I,jetId/I,muonIdx1/I,muonIdx2/I,nConstituents/I,nElectrons/I,nMuons/I,puId/I,genJetIdx/I,hadronFlavour/I,partonFlavour/I,cleanmask/O"
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

nanoDataElectronVarString = "deltaEtaSC/F,dr03EcalRecHitSumEt/F,dr03HcalDepth1TowerSumEt/F,dr03TkSumPt/F,dxy/F,dxyErr/F,dz/F,dzErr/F,eCorr/F,eInvMinusPInv/F,energyErr/F,eta/F,hoe/F,ip3d/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,sip3d/F,mvaTTH/F,charge/I,cutBased/I,jetIdx/I,pdgId/I,photonIdx/I,tightCharge/I,vidNestedWPBitmap/I,convVeto/O,cutBased_HEEP/O,isPFcand/O,lostHits/b,cleanmask/O"
nanoDataMuonVarString     = "dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,mass/F,dxy/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/I,isPFcand/O,mediumId/O,softId/O,tightId/O,cleanmask/O"
nanoDataLeptonVarString   = ','.join( set( nanoDataElectronVarString.split(',') + nanoDataMuonVarString.split(',') ) )
nanoDataTauVarString      = "chargedIso/F,dxy/F,dz/F,eta/F,footprintCorr/F,leadTkDeltaEta/F,leadTkDeltaPhi/F,leadTkPtOverTauPt/F,mass/F,neutralIso/F,phi/F,photonsOutsideSignalCone/F,pt/F,puCorr/F,rawAntiEle/F,rawIso/F,rawMVAnewDM/F,rawMVAoldDM/F,rawMVAoldDMdR03/F,charge/I,decayMode/I,jetIdx/I,rawAntiEleCat/F,idAntiEle/I,idAntiMu/I,idDecayMode/I,idDecayModeNewDMs/I,idMVAnewDM/I,idMVAoldDM/I,idMVAoldDMdR03/I,cleanmask/O"
nanoDataPhotonVarString   = "eta/F,eCorr/F,energyErr/F,hoe/F,mass/F,mvaID/I,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,charge/I,cutBased/I,electronIdx/I,jetIdx/I,pdgId/I,vidNestedWPBitmap/I,electronVeto/O,mvaID_WP80/O,mvaID_WP90/O,pixelSeed/O,cleanmask/O"
nanoDataJetVarString      = "area/F,btagCMVA/F,btagCSVV2/F,btagDeepB/F,btagDeepC/F,chEmEF/F,chHEF/F,eta/F,mass/F,neEmEF/F,neHEF/F,phi/F,pt/F,qgl/F,rawFactor/F,bReg/F,electronIdx1/I,electronIdx2/I,jetId/I,muonIdx1/I,muonIdx2/I,nConstituents/I,nElectrons/I,nMuons/I,puId/I,cleanmask/O"
nanoDataBJetVarString     = 'pt/F,eta/F,phi/F'

nanoDataElectronVars = [item.split('/')[0] for item in nanoDataElectronVarString.split(',')]
nanoDataMuonVars     = [item.split('/')[0] for item in nanoDataMuonVarString.split(',')]
nanoDataLeptonVars   = [item.split('/')[0] for item in nanoDataLeptonVarString.split(',')]
nanoDataTauVars      = [item.split('/')[0] for item in nanoDataTauVarString.split(',')] 
nanoDataPhotonVars   = [item.split('/')[0] for item in nanoDataPhotonVarString.split(',')]
nanoDataJetVars      = [item.split('/')[0] for item in nanoDataJetVarString.split(',')]
nanoDataBJetVars     = [item.split('/')[0] for item in nanoDataBJetVarString.split(',')]

photonIdCutBased   = { 'fail':0, 'loose':1, 'medium':2, 'tight':3 }              # NanoAOD Version
electronIdCutBased = { 'fail':0, 'veto':1,  'loose':2,  'medium':3, 'tight':4 }  # NanoAOD Version
jetIdBitwise       = { 'fail':0, 'loose':1, 'tight':3 }                          #bitwise (Jet ID flags bit1 is loose, bit2 is tight -> int(00)=0 == fail, int(01)=1 == loose, int(11)=3 == tight)

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
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagCSVV2'] > 0.8484 
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
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
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def filterBJets( jets, tagger = 'DeepCSV', year = 2016 ):
    bJets = list( filter( lambda j: isBJet(j, tagger = tagger, year = year), jets ) )
    bJets.sort( key = lambda j: -j['pt'] )
    return bJets

def muonVertexSelector( l ):
    if abs(l["dxy"]) >= 0.05: return False
    if abs(l["dz"])  >= 0.1:  return False
    return True

def electronVertexSelector( l ):
    EC = abs(l["eta"]) > 1.479
    if abs(l["dxy"])       >= 0.05: return False
    if EC and abs(l["dz"]) >= 0.1:  return False
    return True

def photonIDSelector( p ):
    # still missing: relIso_neutral, relIso_photon  (should be in medium cutbased ID)
    EC = abs(p["eta"]) > 1.479
    if p["hoe"]              >= (0.0396-0.0177*EC):   return False
    if p["sieie"]            >= (0.01022+0.01979*EC): return False
    if p["pfRelIso03_chg"]   >= (0.441+0.001*EC):     return False
    return True

def triggerEmulatorSelector( l ):
    # still missing: dPhiSC, dEtaSC
    ECSc = abs(l["eta"] + l["deltaEtaSC"]) > 1.479
    if l["sieie"]            >= (0.011+0.019*ECSc): return False
#    if abs(l["dPhiScTrkIn"]) >= (0.04+0.03*ECSc):  return False
#    if abs(l["deltaEtaSC"])  >= (0.01-0.002*ECSc): return False
    if l["eInvMinusPInv"]    <= -0.05:              return False
    if l["eInvMinusPInv"]    >= (0.01-0.005*ECSc):  return False
    if l["hoe"]              >= (0.10-0.03*ECSc):   return False
    return True

def barrelEndcapVeto( p ):
    return ( abs(p["eta"]) > 1.556 or abs(p["eta"]) <= 1.4442 )

# Reco Selectors
def jetSelector():
    # According to AN-2017/197
    # hadron multiplicity > 0 still missing
    def func(j):
        if j["pt"]            <= 30:   return False
        if abs(j["eta"])      >= 2.4:  return False
        if j["nConstituents"]  < 2:    return False
        if j["neHEF"]         >= 0.99: return False
        if j["neEmEF"]        >= 0.99: return False
        if j["chEmEF"]        >= 0.99: return False
        if j["chHEF"]         <= 0.:   return False
        if j["jetId"]          < jetIdBitwise['loose']: return False
        return True
    return func

def muonSelector( lepton_selection ):
    # According to AN-2017/197
    # muon veto: softId should be vetoId
    if lepton_selection == 'tight':
        def func(l):
            if l["pt"]             <= 25:   return False
            if abs(l["eta"])       >= 2.4:  return False
            if l['pfRelIso03_all'] >= 0.12: return False
            if l["sip3d"]          >= 4:    return False
            if not muonVertexSelector(l):   return False
            if not l["mediumId"]:           return False
            return True
        return func

    if lepton_selection == 'loose':
        def func(l):
            if l["pt"]             <= 15:   return False
            if abs(l["eta"])       >= 2.4:  return False
            if l['pfRelIso03_all'] >= 0.12: return False
            if l["sip3d"]          >= 4:    return False
            if not muonVertexSelector(l):   return False
            if not l["mediumId"]:           return False
            return True
        return func

    elif lepton_selection == 'veto':
        def func(l):
            if l["pt"]             <= 15:   return False
            if abs(l["eta"])       >= 2.4:  return False
            if l['pfRelIso03_all'] >= 0.4:  return False
            if l["sip3d"]          >= 4:    return False
            if not muonVertexSelector(l):   return False
            return True
        return func

# electrons 
def eleSelector( lepton_selection, year=2016 ):
    # According to AN-2017/197
    # still missing: MVA
    idVar = "cutBased" if year==2016 else "cutBasedBitmap"
    if lepton_selection == 'tight':
        def func(l):
            if l["pt"]             <= 25:              return False
            if abs(l["eta"])       >= 2.4:             return False
            if l['pfRelIso03_all'] >= 0.12:            return False
            if l["sip3d"]          >= 4:               return False
            if ord(l["lostHits"])  != 0:               return False
            if not l["convVeto"]:                      return False
            if not electronVertexSelector(l):          return False
            if not triggerEmulatorSelector(l):         return False
            if l[idVar] < electronIdCutBased['loose']: return False
            return True
        return func

    if lepton_selection == 'loose':
        def func(l):
            if l["pt"]             <= 15:              return False
            if abs(l["eta"])       >= 2.4:             return False
            if l['pfRelIso03_all'] >= 0.12:            return False
            if l["sip3d"]          >= 4:               return False
            if ord(l["lostHits"])  != 0:               return False
            if not l["convVeto"]:                      return False
            if not electronVertexSelector(l):          return False
            if not triggerEmulatorSelector(l):         return False
            if l[idVar] < electronIdCutBased['loose']: return False
            return True
        return func

    elif lepton_selection == 'veto':
        def func(l):
            if l["pt"]             <= 15:              return False
            if abs(l["eta"])       >= 2.4:             return False
            if l['pfRelIso03_all'] >= 0.4:             return False
            if l["sip3d"]          >= 4:               return False
            if not electronVertexSelector(l):          return False
            if l[idVar] < electronIdCutBased['loose']: return False
            return True
        return func

def tauSelector( lepton_selection ):
    # dummy function
        def func(l):
            return True
        return func

def photonSelector( selection, year=2016 ):
    # According to AN-2017/197
    idVar = "cutBased" if year==2016 else "cutBasedBitmap"
    if selection == 'medium':
        def func(g):
            if g["pt"]             <= 20:              return False
            if abs(g["eta"])       >= 1.479:           return False
            if not g["pixelSeed"]:                     return False
#            if not barrelEndcapVeto(g):                return False
            if not photonIDSelector(g):                return False
            if not g["electronVeto"]:                  return False
            if g[idVar] < photonIdCutBased[selection]: return False
            return True
        return func

    if selection == 'forward':
        def func(g):
            if g["pt"]             <= 20:              return False
            if abs(g["eta"])        < 1.479:           return False
            if not g["pixelSeed"]:                     return False
            if not barrelEndcapVeto(g):                return False
            if not photonIDSelector(g):                return False
            if not g["electronVeto"]:                  return False
            if g[idVar] < photonIdCutBased['medium']:  return False
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

# check for nanoAOD
def getFilterCut( isData=False, isFastSim=False, year=2016, ignoreJSON=False ):
    if isFastSim:
        filters             = [ "Flag_goodVertices" ]
    elif year == 2016:
        filters             = [ "Flag_goodVertices", "Flag_HBHENoiseIsoFilter", "Flag_HBHENoiseFilter" ]
        filters            += [ "Flag_globalTightHalo2016Filter", "Flag_EcalDeadCellTriggerPrimitiveFilter" ]
#        filters            += [ "Flag_badChargedHadronSummer2016", "Flag_badMuonSummer2016" ]
        filters            += [ "Flag_muonBadTrackFilter", "Flag_chargedHadronTrackResolutionFilter" ]
#        filters            += [ "Flag_METFilters" ]
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]
    elif year == 2017:
        filters             = [ "Flag_goodVertices", "Flag_globalTightHalo2016Filter" ]
        filters            += [ "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter" ]
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_BadPFMuonFilter", "Flag_BadChargedCandidateFilter", "Flag_ecalBadCalibFilter" ]
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]
    if isData:
        filters += [ "weight>0" ]
        if not ignoreJSON:
            filters += [ "jsonPassed>0" ]
    return "&&".join(filters)

