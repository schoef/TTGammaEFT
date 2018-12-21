#nanoAOD postprocessing Autumn2018

python nanoPostProcessing.py --overwrite --skim semilep --year 2018 --processingEra TTGammaEFT_PP_2018_TTG_v1 --sample TTLep_pow                  --fileBasedSplitting #SPLIT137
python nanoPostProcessing.py --overwrite --skim semilep --year 2018 --processingEra TTGammaEFT_PP_2018_TTG_v1 --sample DYJetsToLL_M50_LO          --fileBasedSplitting #SPLIT4
python nanoPostProcessing.py --overwrite --skim semilep --year 2018 --processingEra TTGammaEFT_PP_2018_TTG_v1 --sample DYJetsToLL_M50             --fileBasedSplitting #SPLIT112
python nanoPostProcessing.py --overwrite --skim semilep --year 2018 --processingEra TTGammaEFT_PP_2018_TTG_v1 --sample WW                         --fileBasedSplitting #SPLIT23
python nanoPostProcessing.py --overwrite --skim semilep --year 2018 --processingEra TTGammaEFT_PP_2018_TTG_v1 --sample GluGluToContinToZZTo2e2mu  --fileBasedSplitting #SPLIT16
python nanoPostProcessing.py --overwrite --skim semilep --year 2018 --processingEra TTGammaEFT_PP_2018_TTG_v1 --sample GluGluToContinToZZTo2e2tau --fileBasedSplitting #SPLIT15
