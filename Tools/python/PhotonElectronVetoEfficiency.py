import ROOT
import os

from TTGammaEFT.Tools.helpers import getObjFromFile
from TTGammaEFT.Tools.u_float import u_float

# Logging
import logging
logger = logging.getLogger(__name__)

g_keys = [( "ScalingFactors_80X_Summer16.root", "Scaling_Factors_CSEV_R9 Inclusive"   ),
          ( "ScalingFactors_80X_Summer16.root", "Scaling_Factors_HasPix_R9 Inclusive" )]

class PhotonElectronVetoEfficiency:
    def __init__(self):
        self.dataDir = "$CMSSW_BASE/src/TTGammaEFT/Tools/data/photonSFData"
        self.g_sf = [ getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in g_keys ]
        for effMap in self.g_sf: assert effMap

    def getPartialSF(self, effMap, pt, eta):
        sf  = effMap.GetBinContent( effMap.FindBin(eta, pt) )
        err = effMap.GetBinError(   effMap.FindBin(eta, pt) )
        return u_float(sf, err)

    def mult(self, list):
        res = list[0]
        for i in list[1:]: res = res*i
        return res

    def getSF(self, pt, eta, sigma=0):
        if pt       >= 200: pt  = 199
        if abs(eta) >= 2.5: eta = 2.49 

        sf = self.mult([self.getPartialSF(effMap, pt, abs(eta)) for effMap in self.g_sf])

        return (1+sf.sigma*sigma)*sf.val

