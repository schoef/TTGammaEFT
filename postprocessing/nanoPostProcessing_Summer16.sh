#nanoAOD postprocessing Summer2016

python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TTGLep                 --fileBasedSplitting #SPLIT7
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TTbar                  --fileBasedSplitting #SPLIT55
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample ZGToLLG                --fileBasedSplitting #SPLIT10
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample ZGTo2LG_ext            --fileBasedSplitting #SPLIT10
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample T_tWch_ext             --fileBasedSplitting #SPLIT8
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TBar_tWch_ext          --fileBasedSplitting #SPLIT9
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample DYJetsToLL_M50_LO_ext1 --fileBasedSplitting #SPLIT34
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample DYJetsToLL_M10to50_LO  --fileBasedSplitting #SPLIT34

python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TTLep_pow              --fileBasedSplitting #SPLIT63
python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TTGJets_ext            --fileBasedSplitting #SPLIT13

# not necessary ATM
#python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TTGSemiT               --fileBasedSplitting #SPLIT
#python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TTGSemiTbar            --fileBasedSplitting #SPLIT13
#python nanoPostProcessing.py --overwrite --skim dilep --year 2016 --processingEra TTGammaEFT_PP_2016_TTG_v1 --sample TTGHad                 --fileBasedSplitting #SPLIT
