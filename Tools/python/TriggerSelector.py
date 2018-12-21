# Problems with HLT_DoubleEle33_CaloIdL_GsfTrkIdVL, HLT_TkMu50 and HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL

class TriggerSelector:
    def __init__( self, year, singleLepton=False ):

        if year == 2016:
            if singleLepton:
                self.m  = [ "HLT_IsoMu24", "HLT_IsoTkMu24" ]
                self.e  = [ "HLT_Ele32_eta2p1_WPTight_Gsf" ]
                self.mm = None
                self.em = None
                self.ee = None
            else:
                self.mm = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ", "HLT_Mu30_TkMu11" ]
#                self.m  = [ "HLT_IsoMu24", "HLT_IsoTkMu24", "HLT_Mu50", "HLT_TkMu50", "HLT_Mu45_eta2p1" ] #HLT_IsoTkMu24, HLT_IsoMu24
                self.m  = [ "HLT_IsoMu24", "HLT_IsoTkMu24", "HLT_Mu50", "HLT_Mu45_eta2p1" ] #HLT_IsoTkMu24, HLT_IsoMu24
#                self.ee = [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL", "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW" ]
                self.ee = [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW" ]
                self.e  = [ "HLT_Ele27_WPTight_Gsf", "HLT_Ele105_CaloIdVT_GsfTrkIdT", "HLT_Ele115_CaloIdVT_GsfTrkIdT" ] #HLT_Ele105_CaloIdVT_GsfTrkIdT
#                self.em = [ "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL", "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL" ]
                self.em = [ "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL"]

        # not adapted yet
        elif year == 2017:
            if singleLepton:
                self.m  = [ "HLT_IsoMu24" ]
                self.e  = [ "HLT_Ele27_WPTight_Gsf" ]
                self.mm = None
                self.em = None
                self.ee = None
            else:
                self.mm = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8"] # "HLT_Mu37_TkMu27" not in nanoAOD
                self.m  = ["HLT_IsoMu27", "HLT_Mu50"]
                self.ee = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"]
                self.e  = ["HLT_Ele35_WPTight_Gsf", "HLT_Ele32_WPTight_Gsf_L1DoubleEG"] # add single photon trigger? "HLT_Ele115_CaloIdVT_GsfTrkIdT" missing
                self.em = ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ"]

        # not adapted yet
        elif year == 2018:
            if singleLepton:
                self.m  = [ "HLT_IsoMu24" ]
                self.e  = [ "HLT_Ele27_WPTight_Gsf" ]
                self.mm = None
                self.em = None
                self.ee = None
            else:
                self.mm = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8", "HLT_Mu37_TkMu27"]
                self.m  = ["HLT_IsoMu24", "HLT_IsoMu27", "HLT_Mu50"]
                self.ee = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"]
                self.e  = ["HLT_Ele32_WPTight_Gsf", "HLT_Ele115_CaloIdVT_GsfTrkIdT", "HLT_Ele32_WPTight_Gsf_L1DoubleEG"]
                self.em = ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu27_Ele37_CaloIdL_MW", "HLT_Mu37_Ele27_CaloIdL_MW"]

        else:
            raise NotImplementedError( "Trigger selection %r not implemented" %year )

        # define which triggers should be used for which dataset
        self.DoubleMuon     = "(%s)"%"||".join( self.mm ) if self.mm else None
        self.DoubleEG       = "(%s)"%"||".join( self.ee ) if self.ee else None
        self.MuonEG         = "(%s)"%"||".join( self.em ) if self.em else None
        self.SingleMuon     = "(%s)"%"||".join( self.m  ) if self.m  else None
        self.SingleElectron = "(%s)"%"||".join( self.e  ) if self.e  else None

        # define an arbitrary hierarchy
        self.PDHierarchy = [ "DoubleMuon", "DoubleEG", "MuonEG", "SingleMuon", "SingleElectron" ]

    def __getVeto( self, cutString ):
        return "!%s" %cutString

    def getAllTrigger( self ):
        return self.mm + self.m + self.ee + self.e + self.em

    def getSelection( self, PD ):
        found     = False
        cutString = ""

        if PD == "MC":
            triggerList = [ item for item in [ self.DoubleMuon, self.DoubleEG, self.MuonEG, self.SingleMuon, self.SingleElectron ] if item ]
            return "(%s)"%"||".join( triggerList )
        else:
            for x in reversed( self.PDHierarchy ):
                if not getattr( self, x ): continue # Trigger not included (singleLepton)
                if found:
                    cutString += "&&%s" %self.__getVeto( getattr( self, x ) )
                if x in PD:
                    found      = True
                    cutString  = getattr( self, x )

            if cutString == "":
                raise NotImplementedError( "Trigger selection for %s not implemented" %PD )

            return "(%s)" %cutString
