''' Class to interpret string based cuts
'''

# TTGamma Imports
from TTGammaEFT.Tools.constants    import mZ
from TTXPheno.Tools.CutInterpreter import CutInterpreter

special_cuts = {
    "looseLeptonVeto":   "nLeptonVeto==2",
    "dilep":             "nLepton==2&&nLeptonTight>=1",
    "dilepOS":           "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])<0",
    "dilepSS":           "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])>0",
    "dilepOFOS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])<0&&nElectron==1&&nMuon==1",
    "dilepOFSS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])>0&&nElectron==1&&nMuon==1",
    "dilepSFOS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])<0&&(nElectron==2||nMuon==2)",
    "dilepSFSS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])>0&&(nElectron==2||nMuon==2)",
    "offZ":              "abs(mll-%s)>15&&abs(mllgamma-%s)>15"%(mZ,mZ),
    "offZSF":            "abs(mll-%s)>15&&abs(mllgamma-%s)>15&&((nElectron==2||nMuon==2)||(nElectron==1&&nMuon==1))"%(mZ,mZ),   # Cut Z-Window only for SF dilep events
    "onZ":               "abs(mllgamma-%s)<15"%(mZ),
    "onZSF":             "abs(mllgamma-%s)<15&&((nElectron==2||nMuon==2)||(nElectron==1&&nMuon==1))"%(mZ),                      # Cut Z-Window only for SF dilep events
    "mumu":              "nElectron==0&&nMuon==2",
    "mue":               "nElectron==1&&nMuon==1",
    "ee":                "nElectron==2&&nMuon==0",
    "all":               "(1)",
    "SF":                "(nElectron==2||nMuon==2)",
    "dilepPP":           "Sum$(Electron_pt>15&&abs(Electron_eta)<2.5)+Sum$(Muon_pt>15&&abs(Muon_eta)<2.5)==2&&Sum$(Electron_pt>25&&abs(Electron_eta)<2.5)+Sum$(Muon_pt>25&&abs(Muon_eta)<2.5)>=1",
  }

continous_variables = [ ("metSig", "metSig"), ("mll", "mll"), ("mllgamma", "mllgamma"), ("met", "MET_pt"), ("pTG","Photon_pt[0]") ]
discrete_variables  = [ ("nJet", "nJet"), ("nBTag", "nBTag"), ("nbtagPP", "Sum$(Jet_btagCSVV2>0.8484)"), ("nLepVeto","nLeptonVeto"), ("nLepTight","nLeptonTight"), ("nLep","nLepton"), ("nPhoton","nPhoton") ]

cutInterpreter = CutInterpreter( continous_variables, discrete_variables, special_cuts)

if __name__ == "__main__":
    print cutInterpreter.cutString("dilepOS-pTG20-nPhoton1p-offZSF-mll40")

