nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py --small --noData --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSF-mll40" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py --small --noData --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-onZSF-mll40" &

nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py --noData --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-offZSF-mll40" &
nohup krenew -t -K 10 -- bash -c "python analysisPlots2016.py --noData --selection dilepOS-nLepVeto2-pTG20-nPhoton1p-onZSF-mll40" &
