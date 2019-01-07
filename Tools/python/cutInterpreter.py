''' Class to interpret string based cuts
'''

# TTGamma Imports
from TTGammaEFT.Tools.constants    import mZ
from TTXPheno.Tools.CutInterpreter import CutInterpreter

special_cuts = {
    "OS":                "(LeptonGood_pdgId[0]*LeptonGood_pdgId[1])<0",
    "looseLeptonVeto":   "nLeptonVeto==2",
    "dilep":             "nLeptonGood==2&&nLeptonTight>=1",
    "dilepOS":           "nLeptonGood==2&&nLeptonTight>=1&&(LeptonGood_pdgId[0]*LeptonGood_pdgId[1])<0",
    "dilepSS":           "nLeptonGood==2&&nLeptonTight>=1&&(LeptonGood_pdgId[0]*LeptonGood_pdgId[1])>0",
    "dilepOFOS":         "nLeptonGood==2&&nLeptonTight>=1&&(LeptonGood_pdgId[0]*LeptonGood_pdgId[1])<0&&nElectronGood==1&&nMuonGood==1",
    "dilepOFSS":         "nLeptonGood==2&&nLeptonTight>=1&&(LeptonGood_pdgId[0]*LeptonGood_pdgId[1])>0&&nElectronGood==1&&nMuonGood==1",
    "dilepSFOS":         "nLeptonGood==2&&nLeptonTight>=1&&(LeptonGood_pdgId[0]*LeptonGood_pdgId[1])<0&&(nElectronGood==2||nMuonGood==2)",
    "dilepSFSS":         "nLeptonGood==2&&nLeptonTight>=1&&(LeptonGood_pdgId[0]*LeptonGood_pdgId[1])>0&&(nElectronGood==2||nMuonGood==2)",
    "offZll":            "abs(mll-%s)>15"%(mZ),
    "offZllg":           "abs(mllgamma-%s)>15"%(mZ),
    "offZSFll":          "((abs(mll-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                      # Cut Z-Window only for SF dilep events
    "offZSFllg":         "((abs(mllgamma-%s)>15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                 # Cut Z-Window only for SF dilep events
    "onZll":             "abs(mll-%s)<=15"%(mZ),
    "onZllg":            "abs(mllgamma-%s)<=15"%(mZ),
    "onZSFll":           "((abs(mll-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                     # Cut Z-Window only for SF dilep events
    "onZSFllg":          "((abs(mllgamma-%s)<=15&&(nElectronGood==2||nMuonGood==2))||(nElectronGood==1&&nMuonGood==1))"%(mZ),                # Cut Z-Window only for SF dilep events
    "mumu":              "nElectronGood==0&&nMuonGood==2",
    "mue":               "nElectronGood==1&&nMuonGood==1",
    "ee":                "nElectronGood==2&&nMuonGood==0",
    "all":               "(1)",
    "SF":                "(nElectronGood==2||nMuonGood==2)",
    "dPhiJet0":          "Sum$((cos(MET_phi-JetGood_phi)>0.8)*(Iteration$==0))==0",
    "dPhiJet1":          "Sum$((cos(MET_phi-JetGood_phi)>cos(0.25))*(Iteration$<2))==0",
  }

continous_variables = [ ("metSig", "metSig"), ("mll", "mll"), ("mllgamma", "mllgamma"), ("met", "MET_pt"), ("pTG","PhotonGood_pt[0]") ]
discrete_variables  = [ ("nJet", "nJetGood"), ("nBTag", "nBTagGood"), ("nLepVeto","nLeptonVeto"), ("nLepTight","nLeptonTight"), ("nLep","nLeptonGood"), ("nPhoton","nPhotonGood") ]

cutInterpreter = CutInterpreter( continous_variables, discrete_variables, special_cuts)

if __name__ == "__main__":
    print cutInterpreter.cutString("dilepOS-pTG20-nPhoton1p-offZSF-mll40")

