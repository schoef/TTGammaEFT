small=""
#small="--small"
noData=""
#noData="--noData"

# Base line selection
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40    --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots" &

# Control region
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-offZSFll-mll40                             --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-mll40                                      --plot_directory 80X_TTG_ppv5_v1 --plotFile mllPlots" &

# Basic checks
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection nJet2p-nBTag1p-nLepVeto2-mll20-dPhiJet0-dPhiJet1-offZSFll-OS --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots_StopsDilepton" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection nJet2p-nBTag1p-nLepVeto2-mll20-offZSFll-OS --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots_StopsDilepton" &

# Signal regions
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag0  --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1  --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag2p --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet1-nBTag1   --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots" &

# For fun
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 80X_TTG_ppv5_v1 --plotFile allPlots" &
