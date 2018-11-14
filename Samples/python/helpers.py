''' Helpers Functions
'''
# Imports
from RootTools.core.Sample import Sample

#
# Helpers Functions
#
def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

def getSample( pd, runName, lumi ):
    sample  = Sample.fromDirectory( name=( pd + '_' + runName ), treeName="Events", texName=( pd + ' (' + runName + ')' ), directory=dirs[ pd + '_' + runName ] )
    sample.lumi = lumi
    return sample

