''' Class to interpret string based cuts
'''

special_cuts = {
    "looseLeptonVeto":   "nLeptonVeto==2",
    "dilepOS":           "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])<0",
    "dilepSS":           "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])>0",
    "dilepOFOS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])<0&&nElectron==1&&nMuon==1",
    "dilepOFSS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])>0&&nElectron==1&&nMuon==1",
    "dilepSFOS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])<0&&(nElectron==2||nMuon==2)",
    "dilepSFSS":         "nLepton==2&&nLeptonTight>=1&&(Lepton_pdgId[0]*Lepton_pdgId[1])>0&&(nElectron==2||nMuon==2)",
    "offZ":              "abs(mll-91.2)>15&&abs(mllgamma-91.2)>15",
    "offZSF":            "abs(mll-91.2)>15&&abs(mllgamma-91.2)>15&&((nElectron==2||nMuon==2)||(nElectron==1&&nMuon==1))",#cut Z-Window only for SF dilep events
  }

continous_variables = [ ("metSig", "metSig"), ("mll", "mll"), ("mllgamma", "mllgamma"), ("met", "MET_pt"), ("pTG","Photon_pt[0]") ]
discrete_variables  = [ ("nJet", "nJet"), ("nBTag", "nBTag") , ("nLepVeto","nLeptonVeto"), ("nLepTight","nLeptonTight"), ("nLep","nLepton"), ("nPhoton","nPhoton") ]

from TTXPheno.Tools.CutInterpreter import CutInterpreter
cutInterpreter = CutInterpreter( continous_variables, discrete_variables, special_cuts)

if __name__ == "__main__":
    print cutInterpreter.cutString("dilepOS-pTG20-nPhoton1p-offZSF-mll40")

