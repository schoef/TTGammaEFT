small=""
#small="--small"
noData=""
#noData="--noData"

# Base line selection
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40    --plot_directory 80X_TTG_ppv1_v2 --plotFile test" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20               --plot_directory 80X_TTG_ppv1_v2 --plotFile test" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40    --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-offZSFll-nJet2p-nBTag1p-mll20               --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFll-mll40              --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-onZSFll-mll40               --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-onZSFllg-onZSFll-mll40      --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &

# Control region
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-offZSFll-mll40                             --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-mll40                      --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &

# Basic checks
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection nJet2p-nBTag1p-nLepVeto2-mll20-dPhiJet0-dPhiJet1-offZSFll-OS --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection nJet2p-nBTag1p-nLepVeto2-mll20-offZSFll-OS                    --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection nJet2p-nBTag1p-nLepVeto2-mll20-OS                             --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &

# Signal regions
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag0  --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1  --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag2p --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet1-nBTag1   --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &

# For fun
#nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py ${small} ${noData} --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSFllg-offZSFll-mll40-nJet2p-nBTag1p --plot_directory 80X_TTG_ppv1_v2 --plotFile all" &
