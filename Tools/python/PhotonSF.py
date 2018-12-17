import ROOT
import os

from TTGammaEFT.Tools.helpers import getObjFromFile
from TTGammaEFT.Tools.u_float import u_float

# Logging
import logging
logger = logging.getLogger(__name__)

class PhotonSF:
    def __init__(self, year=2016):

        self.year    = year
        self.dataDir = "$CMSSW_BASE/src/TTGammaEFT/Tools/data/photonSFData"

        if self.year == 2016:
            g_file = self.dataDir + '/2016LegacyReReco_PhotonCutBasedMedium.root'
            g_key  = "EGamma_SF2D"

        self.g_sf = getObjFromFile( os.path.expandvars(g_file), g_key)
        assert self.g_sf, "Could not load gamma SF histo %s from file %s."%( g_key, g_file )

        self.g_ptMax = self.g_sf.GetYaxis().GetXmax()
        self.g_ptMin = self.g_sf.GetYaxis().GetXmin()

        self.g_etaMax = self.g_sf.GetXaxis().GetXmax()
        self.g_etaMin = self.g_sf.GetXaxis().GetXmin()

    def getSF(self, pt, eta, sigma=0):
        if not (eta <= self.g_etaMax):
            logger.warning( "Supercluster eta out of bounds: %3.2f (need %3.2f <= eta <=% 3.2f)", eta, self.g_etaMin, self.g_etaMax )
            eta = self.g_etaMax-0.01
        if not (eta >= self.g_etaMin):
            logger.warning( "Supercluster eta out of bounds: %3.2f (need %3.2f <= eta <=% 3.2f)", eta, self.g_etaMin, self.g_etaMax )
            eta = self.g_etaMin+0.01

        if   pt >= self.g_ptMax: pt = self.g_ptMax - 1
        elif pt <= self.g_ptMin: pt = self.g_ptMin + 1

        val    = self.g_sf.GetBinContent( self.g_sf.FindBin(eta, pt) )
        valErr = self.g_sf.GetBinError(   self.g_sf.FindBin(eta, pt) )

        return val + sigma*valErr

