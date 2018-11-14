import os

if os.environ['USER'] in ['schoef', 'rschoefbeck', 'schoefbeck']:
    results_directory   = "/afs/hephy.at/data/rschoefbeck02/TTGammaEFT/results/"
    skim_output_directory      = "/afs/hephy.at/data/rschoefbeck02/TTGammaEFT/skims/"
    skim_directory      = "/afs/hephy.at/data/dspitzbart01/TTGammaEFT/skims/"
    tmp_directory       = "/afs/hephy.at/data/rschoefbeck02/TTGammaEFT_tmp/"
    plot_directory      = "/afs/hephy.at/user/r/rschoefbeck/www/TTGammaEFT/"
    data_directory      = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
    #data_directory      = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
    #postprocessing_output_directory = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
    postprocessing_output_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
    analysis_results    = results_directory

    runOnGentT2 = False

if os.environ['USER'] in ['llechner']:
    tmp_directory                       = "/afs/hephy.at/data/llechner01/Top_tmp/"
    results_directory                   = "/afs/hephy.at/data/llechner01/TTGammaEFT/results/"
    skim_directory                      = "/afs/hephy.at/data/llechner01/TTGammaEFT/skims/"
    skim_output_directory               = "/afs/hephy.at/data/llechner01/TTGammaEFT/skims/"
    plot_directory                      = "/afs/hephy.at/user/l/llechner/www/TTGammaEFT/"
    data_directory                      = "/afs/hephy.at/data/llechner01/TTGammaEFT/nanoTuples/"
    postprocessing_output_directory     = "/afs/hephy.at/data/llechner01/TTGammaEFT/nanoTuples/"
    analysis_results                    = results_directory
    
    runOnGentT2 = False
