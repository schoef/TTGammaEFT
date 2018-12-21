small="--small"

nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll-mll20 --plot_directory 94X_TTG_ppv3_v2 --plotFile main --normalize" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} --selection dilepOS-nLepVeto2 --plot_directory 94X_TTG_ppv3_v2 --plotFile main --normalize" &

small=""

nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} --selection dilepOS-nLepVeto2-offZSFll-mll20 --plot_directory 94X_TTG_ppv3_v2 --plotFile main --normalize" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2017.py ${small} --selection dilepOS-nLepVeto2 --plot_directory 94X_TTG_ppv3_v2 --plotFile main --normalize" &

