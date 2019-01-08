small=""
#small="--small"
noData=""
#noData="--noData"

# Base line selection
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40 --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20            --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-onZll                                    --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-onZll-nJet1p                             --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
