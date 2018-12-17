import ROOT
import os

from TTGammaEFT.Tools.helpers import getObjFromFile
from TTGammaEFT.Tools.u_float import u_float

keys_mu_BCDEF = [( "RunBCDEF_SF_ID.root",  "NUM_MediumID_DEN_genTracks_eta_pt"   ),
                 ( "RunBCDEF_SF_ISO.root", "NUM_TightRelIso_DEN_MediumID_eta_pt" )]

keys_mu_GH    = [( "RunGH_SF_ID.root",     "NUM_MediumID_DEN_genTracks_eta_pt"   ),
                 ( "RunGH_SF_ISO.root",    "NUM_TightRelIso_DEN_MediumID_eta_pt" )]

# FIX ME
lumiRatio_BCDEF = 19.717640795 / 35.863818448
lumiRatio_GH    = 16.146177653 / 35.863818448

keys_ele      = [( "2016LegacyReReco_ElectronMedium.root", "EGamma_SF2D" )]

class LeptonSF:
    def __init__(self):
        self.dataDir = "$CMSSW_BASE/src/TTGammaEFT/Tools/data/leptonSFData"

        self.mu_BCDEF = [ getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in keys_mu_BCDEF ]
        self.mu_GH    = [ getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in keys_mu_GH    ]
        self.ele      = [ getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in keys_ele      ]

        for effMap in self.mu_BCDEF + self.mu_GH + self.ele: assert effMap

    def getPartialSF(self, effMap, pt, eta):
        sf  = effMap.GetBinContent( effMap.FindBin(eta, pt) )
        err = effMap.GetBinError(   effMap.FindBin(eta, pt) )
        return u_float(sf, err)

    def mult(self, list):
        res = list[0]
        for i in list[1:]: res = res*i
        return res

    def getSF(self, pdgId, pt, eta, sigma=0):
        if abs(pdgId) == 13:
            if   pt  >=  120: pt  =   119
            if   pt  <=   20: pt  =    21
            if   eta >=  2.4: eta =  2.39 
            elif eta <= -2.4: eta = -2.39 

            sf_BCDEF = self.mult( [self.getPartialSF(effMap, pt, eta) for effMap in self.mu_BCDEF] ).val
            sf_GH    = self.mult( [self.getPartialSF(effMap, pt, eta) for effMap in self.mu_GH] ).val
            sf       = (sf_BCDEF*lumiRatio_BCDEF) + (sf_GH*lumiRatio_GH) # Scale SF by lumiRatio
            sigma    = 0.03 # Recommendation for Moriond17
            sf       = u_float(sf, sigma)

        elif abs(pdgId) == 11:
            if   pt  >=  500: pt  =   499
            if   pt  <=   10: pt  =    11
            if   eta >=  2.5: eta =  2.49 
            elif eta <= -2.5: eta = -2.49 

            sf = self.mult([self.getPartialSF(effMap, pt, eta) for effMap in self.ele])

        else:
          raise Exception("Lepton SF for PdgId %i not known"%pdgId)

        return (1+sf.sigma*sigma)*sf.val
