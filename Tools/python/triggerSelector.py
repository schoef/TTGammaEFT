class triggerSelector:
    def __init__( self, year ):
        if year == 2016:
            self.mm     = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ", "HLT_Mu30_TkMu11" ]
            self.m      = [ "HLT_IsoMu24", "HLT_IsoTkMu24", "HLT_Mu50", "HLT_TkMu50", "HLT_Mu45_eta2p1" ]
            self.ee     = [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL", "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW" ]
            self.e      = [ "HLT_Ele27_WPTight_Gsf", "HLT_Ele105_CaloIdVT_GsfTrkIdT", "HLT_Ele115_CaloIdVT_GsfTrkIdT" ]
            self.em     = [ "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL", "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL" ]

        elif year == 2017:
            self.mm     = []
            self.m      = []
            self.ee     = []
            self.e      = []
            self.em     = []

        elif year == 2018:
            self.mm     = []
            self.m      = []
            self.ee     = []
            self.e      = []
            self.em     = []

        else:
            raise NotImplementedError( "Trigger selection %r not implemented" %year )

        # define which triggers should be used for which dataset
        self.DoubleMuon     = "(%s)"%"||".join( self.mm + self.m )
        self.DoubleEG       = "(%s)"%"||".join( self.ee + self.e )
        self.MuonEG         = "(%s)"%"||".join( self.em + self.e + self.m )

        # define an arbitrary hierarchy
        self.PDHierarchy = [ "DoubleMuon", "DoubleEG", "MuonEG" ]

    def __getVeto( self, cutString ):
        return "!%s" %cutString

    def getSelection( self, PD ):
        found     = False
        cutString = ""

        if PD == "MC":
            return "(%s)"%"||".join( [ self.DoubleMuon, self.DoubleEG, self.MuonEG ] )
        else:
            for x in reversed( self.PDHierarchy ):
                if found:
                    cutString += "&&%s" %self.__getVeto( getattr( self, x ) )
                if x in PD:
                    found     = True
                    cutString = getattr( self, x )

            return "(%s)" %cutString
