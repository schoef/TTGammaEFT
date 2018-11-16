
nanoElectronVarString = "deltaEtaSC/F,dr03EcalRecHitSumEt/F,dr03HcalDepth1TowerSumEt/F,dr03TkSumPt/F,dxy/F,dxyErr/F,dz/F,dzErr/F,eCorr/F,eInvMinusPInv/F,energyErr/F,eta/F,hoe/F,ip3d/F,mass/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,sip3d/F,mvaTTH/F,charge/F,cutBased/F,jetIdx/I,pdgId/I,photonIdx/I,tightCharge/I,vidNestedWPBitmap/I,convVeto/I,cutBased_HEEP/I,isPFcand/I,lostHits/I,genPartIdx/I,genPartFlav/I,cleanmask/I"
nanoMuonVarString     = "dxy/F,dxyErr/F,dz/F,dzErr/F,eta/F,mass/F,dxy/F,miniPFRelIso_all/F,miniPFRelIso_chg/F,pfRelIso03_all/F,pfRelIso03_chg/F,pfRelIso04_all/F,phi/F,pt/F,ptErr/F,segmentComp/F,sip3d/F,mvaTTH/F,charge/I,jetIdx/I,nStations/I,nTrackerLayers/I,pdgId/I,tightCharge/I,highPtId/I,isPFcand/I,mediumId/I,softId/I,tightId/I,genPartIdx/I,genPartFlav/I,cleanmask/I"
nanoLeptonVarString   = ','.join( set( nanoElectronVarString.split(',') + nanoMuonVarString.split(',') ) )
nanoTauVarString      = "chargedIso/F,dxy/F,dz/F,eta/F,footprintCorr/F,leadTkDeltaEta/F,leadTkDeltaPhi/F,leadTkPtOverTauPt/F,mass/F,neutralIso/F,phi/F,photonsOutsideSignalCone/F,pt/F,puCorr/F,rawAntiEle/F,rawIso/F,rawMVAnewDM/F,rawMVAoldDM/F,rawMVAoldDMdR03/F,charge/I,decayMode/I,jetIdx/I,rawAntiEleCat/F,idAntiEle/I,idAntiMu/I,idDecayMode/I,idDecayModeNewDMs/I,idMVAnewDM/I,idMVAoldDM/I,idMVAoldDMdR03/I,genPartIdx/I,genPartFlav/I,cleanmask/I"
nanoPhotonVarString   = "eta/F,eCorr/F,energyErr/F,hoe/F,mass/F,mvaID/I,pfRelIso03_all/F,pfRelIso03_chg/F,phi/F,pt/F,r9/F,sieie/F,charge/I,cutBased/I,electronIdx/I,jetIdx/I,pdgId/I,vidNestedWPBitmap/I,electronVeto/I,mvaID_WP80/I,mvaID_WP90/I,pixelSeed/I,genPartIdx/I,genPartFlav/I,cleanmask/I"
nanoJetVarString      = "area/F,btagCMVA/F,btagCSVV2/F,btagDeepB/F,btagDeepC/F,chEmEF/F,chHEF/F,eta/F,mass/F,neEmEF/F,neHEF/F,phi/F,pt/F,qgl/F,rawFactor/F,bReg/F,electronIdx1/I,electronIdx2/I,jetId/I,muonIdx1/I,muonIdx2/I,nConstituents/I,nElectrons/I,nMuons/I,puId/I,genJetIdx/I,hadronFlavour/I,partonFlavour/I,cleanmask/I"
nanoBJetVarString     = 'pt/F,eta/F,phi/F'
nanoGenVarString      = "eta/F,mass/F,pt/F,phi/F,pdgId/I,genPartIdxMother/I,status/I,statusFlags/I"
nanoGenJetVarString   = "eta/F,mass/F,pt/F,phi/F,partonFlavour/F,hadronFlavour/F"

nanoElectronVars = [item.split('/')[0] for item in nanoElectronVarString.split(',')]
nanoMuonVars     = [item.split('/')[0] for item in nanoMuonVarString.split(',')]
nanoLeptonVars   = [item.split('/')[0] for item in nanoLeptonVarString.split(',')]
nanoTauVars      = [item.split('/')[0] for item in nanoTauVarString.split(',')] 
nanoPhotonVars   = [item.split('/')[0] for item in nanoPhotonVarString.split(',')]
nanoJetVars      = [item.split('/')[0] for item in nanoJetVarString.split(',')]
nanoBJetVars     = [item.split('/')[0] for item in nanoBJetVarString.split(',')]
nanoGenVars      = [item.split('/')[0] for item in nanoGenVarString.split(',')]
nanoGenJetVars   = [item.split('/')[0] for item in nanoGenJetVarString.split(',')]

idCutBased       = {'loose':1 ,'medium':2, 'tight':3}

# General Selection Functions
def particlePtEtaSelection( collection, ptCut=10, absEtaCut=2.4 ):
    parts = list( filter( lambda p: p['pt']>ptCut and abs(p['eta']) < absEtaCut, collection ) )
    parts.sort( key = lambda l:-l['pt'] )
    return parts

def jetCleaning( jets, otherParticles, dRCut = 0.4 ):

    from TTGammaEFT.Tools.observables   import deltaR

    res = []
    for jet in jets:
        clean = True
        for otherParticle in otherParticles:
            if deltaR(otherParticle, jet) < dRCut:
                clean = False
                break
        if clean:
            res.append(jet)
    res.sort( key = lambda j:-j['pt'] )
    return res

def getUnsortedParticles( c, collVars, coll ):
    from TTGammaEFT.Tools.helpers           import getVarValue, getObjDict
    return [getObjDict(c, coll+'_', collVars, i) for i in range(int(getVarValue(c, 'n'+coll)))]

def getSortedParticles( c, collVars, coll ):
    part = getUnsortedParticles( c, collVars, coll )
    part.sort( key = lambda l:-l['pt'] )
    return part

def getGoodParticles( selector, coll ):
    part = list( filter( lambda l: selector(l), coll ) )
    part.sort( key = lambda l:-l['pt'] )
    return part
    
def isGoodParticle( p, ptCut=10, absEtaCut=2.4 ):
    return p['pt']>ptCut and abs(p['eta'])<absEtaCut

# Reco Leptons
def getLeptons(c, eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon"):
    leptons  = getSortedParticles( c, eleCollVars,  eleColl  )
    leptons += getSortedParticles( c, muonCollVars, muonColl )
    leptons.sort( key = lambda l:-l['pt'] )
    return leptons

def getGoodLeptons(c, eleSelector, muonSelector, eleCollVars=nanoElectronVars, eleColl="Electron", muonCollVars=nanoMuonVars, muonColl="Muon"):
    leptons  = getGoodParticles( eleSelector,  getSortedParticles( c, eleCollVars,  eleColl  ) )
    leptons += getGoodParticles( muonSelector, getSortedParticles( c, muonCollVars, muonColl ) )
    leptons.sort( key = lambda l:-l['pt'] )
    return leptons

# Reco b-Jet Filter
def isBJet(j, tagger = 'DeepCSV', year = 2016):
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

# Reco Selectors
def jetSelector():
    # According to AN-2017/197
    # hadron multiplicity > 0 still missing
    def func(l):
        return \
            l["pt"]                 > 30 \
            and abs(l["eta"])       < 2.4 \
            and l["nConstituents"]  > 1 \
            and l["neHEF"]          < 0.99 \
            and l["neEmEF"]         < 0.99 \
            and l["chEmEF"]         < 0.99 \
            and l["chHEF"]          > 0.
    return func

def muonSelector( lepton_selection ):
    # According to AN-2017/197
    if lepton_selection == 'tight':
        def func(l):
            return \
                l["pt"]                 > 25 \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.12 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 \
                and l["mediumId"]
        return func

    if lepton_selection == 'loose':
        def func(l):
            return \
                l["pt"]                 > 15 \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.12 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 \
                and l["mediumId"]
        return func

    elif lepton_selection == 'thirdVeto':
        # still missing: veto muon id
        def func(l):
            return \
                l["pt"]                 > 15 \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.4 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 
        return func

# electrons 
def eleSelector( lepton_selection ):
    # According to AN-2017/197
    # still missing: trigger emulation, susy loose id, deltaPhiSC
    if lepton_selection == 'tight':
        def func(l):
            return \
                l["pt"]                 > 25 \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.12 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 \
                and l["convVeto"] \
                and l["lostHits"]       == 0 \
                and ((l['sieie'] < 0.011 and abs(l["eta"]) < 1.479) or (l['sieie'] < 0.03 and abs(l["eta"]) > 1.479)) \
                and ((abs(l['deltaEtaSC']) < 0.01 and abs(l["eta"]) < 1.479) or (abs(l['deltaEtaSC']) < 0.008 and abs(l["eta"]) > 1.479)) \
                and ((l['hoe'] < 0.1 and abs(l["eta"]) < 1.479) or (l['hoe'] < 0.07 and abs(l["eta"]) > 1.479)) \
                and ((l['eInvMinusPInv'] < 0.01 and abs(l["eta"]) < 1.479) or (l['eInvMinusPInv'] < 0.005 and abs(l["eta"]) > 1.479)) \
                and l['eInvMinusPInv'] > -0.05 
        return func

    if lepton_selection == 'loose':
        def func(l):
            return \
                l["pt"]                 > 15 \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.12 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1 \
                and l["convVeto"] \
                and l["lostHits"]       == 0 \
                and ((l['sieie'] < 0.011 and abs(l["eta"]) < 1.479) or (l['sieie'] < 0.03 and abs(l["eta"]) > 1.479)) \
                and ((abs(l['deltaEtaSC']) < 0.01 and abs(l["eta"]) < 1.479) or (abs(l['deltaEtaSC']) < 0.008 and abs(l["eta"]) > 1.479)) \
                and ((l['hoe'] < 0.1 and abs(l["eta"]) < 1.479) or (l['hoe'] < 0.07 and abs(l["eta"]) > 1.479)) \
                and ((l['eInvMinusPInv'] < 0.01 and abs(l["eta"]) < 1.479) or (l['eInvMinusPInv'] < 0.005 and abs(l["eta"]) > 1.479)) \
                and l['eInvMinusPInv'] > -0.05
        return func

    elif lepton_selection == 'thirdVeto':
        # still missing: cut based veto id
        def func(l):
            return \
                l["pt"]                 > 15 \
                and abs(l["eta"])       < 2.4 \
                and l['pfRelIso03_all'] < 0.1 \
                and l["sip3d"]          < 4.0 \
                and abs(l["dxy"])       < 0.05 \
                and abs(l["dz"])        < 0.1
        return func

def tauSelector( lepton_selection ):
    # dummy function
        def func(l):
            return True
        return func

def photonSelector( photon_selection ):
    # According to AN-2017/197
    # still missing: pfRelIso03_neutral
    if photon_selection == 'loose':
        def func(g):
            return \
                g["pt"]                 > 20 \
                and abs(g["eta"])       < 2.4 \
                and ((g['hoe'] < 0.0396 and abs(g["eta"]) < 1.479) or (g['hoe'] < 0.0219 and abs(g["eta"]) > 1.479)) \
                and ((g['pfRelIso03_chg'] < 0.441 and abs(g["eta"]) < 1.479) or (g['pfRelIso03_chg'] < 0.442 and abs(g["eta"]) > 1.479)) \
                and ((g['pfRelIso03_all'] < 2.571+0.0047*(g['pt']**2) and abs(g["eta"]) < 1.479) or (g['pfRelIso03_all'] < 3.863+0.0034*(g['pt']**2) and abs(g["eta"]) > 1.479)) \
                and g["pixelSeed"] \
                and ((g['sieie'] < 0.01022 and abs(g["eta"]) < 1.479) or (g['sieie'] < 0.03001 and abs(g["eta"]) > 1.479)) 
        return func

# Gen Selectors
def genJetSelector():
    # According to AN-2017/197
    def func(l):
        return \
            l["pt"]                 > 30 \
            and abs(l["eta"])       < 2.4
    return func

def genLeptonSelector():
    # According to AN-2017/197
    def func(l):
        return \
            l["pt"]                 > 15 \
            and abs(l["eta"])       < 2.4
    return func

def genPhotonSelector( photon_selection = None ):
    # According to AN-2017/197
    if photon_selection == 'overlapTTGamma':
        def func(g):
            return \
                g["pt"]                 > 13 \
                and abs(g["eta"])       < 3.0
        return func

    if photon_selection == 'overlapZGamma':
        def func(g):
            return \
                g["pt"]                 > 15 \
                and abs(g["eta"])       < 2.6
        return func

    if photon_selection is None:
        def func(l):
            return \
                l["pt"]                 > 13 \
                and abs(l["eta"])       < 2.4
        return func

# Gen Particle Filter
def filterGenElectrons( genParts ):
    electrons = list( filter( lambda l: abs(l['pdgId']) == 11 and l['status'] in [1,23], genParts ) )
    electrons.sort( key = lambda l:-l['pt'] )
    return electrons

def filterGenMuons( genParts ):
    muons = list( filter( lambda l: abs(l['pdgId']) == 13 and l['status'] in [1,23], genParts ) )
    muons.sort( key = lambda l:-l['pt'] )
    return muons

def filterGenPhotons( genParts ):
    photons = list( filter( lambda l: abs(l['pdgId']) == 22 and l['status'] in [1,23], genParts ) )
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
#  1: stage of event generation inside PYTHIA (last particle, even after 23)
# 22: intermediate (intended to have preserved mass) (tops)

# check for nanoAOD
def getFilterCut( isData=False, isFastSim=False, year=2016):
    if isFastSim:
        filters = [ "Flag_goodVertices" ]
    elif year == 2016:
        filters             = [ "Flag_goodVertices", "Flag_HBHENoiseIsoFilter", "Flag_HBHENoiseFilter" ]
        filters            += [ "Flag_globalTightHalo2016Filter", "Flag_EcalDeadCellTriggerPrimitiveFilter" ]
        filters            += [ "Flag_badChargedHadronSummer2016", "Flag_badMuonSummer2016" ]
    elif year == 2017:
        filters             = [ "Flag_goodVertices", "Flag_globalTightHalo2016Filter" ]
        filters            += [ "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter" ]
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_BadPFMuonFilter", "Flag_BadChargedCandidateFilter", "Flag_ecalBadCalibFilter" ]
        if isData: filters += [ "Flag_eeBadScFilter" ]
    if isData: filters += [ "weight>0" ]
#    return "&&".join(filters)
    return "(1)"


