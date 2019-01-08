#!/bin/bash

#declare -a cards=("TTGamma_SingleLeptFromT_3LineBuggy" "TTGamma_SingleLeptFromT_3LinePatched" "TTGamma_SingleLeptFromT_1Line" )
declare -a cards=("TTGamma_SingleLeptFromT_3LineBuggy_full" "TTGamma_SingleLeptFromT_3LinePatched_full" "TTGamma_SingleLeptFromT_1Line_full" )

model="dim6top_LO"

#################################################

for card in "${cards[@]}"
do

    nohup krenew -t -K 10 -- bash -c "getDiagrams.py --process ${card} --model ${model} --overwrite" > logs/${card}.log 2>&1 &

done


