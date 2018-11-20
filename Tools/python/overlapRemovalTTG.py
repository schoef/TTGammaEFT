from TTGammaEFT.Tools.objectSelection import isGoodParticle
from TTGammaEFT.Tools.observables     import deltaR

def isIsolatedPhoton( g, genparts, coneSize=0.2, ptCut=5 ):
    for other in genparts:
      if other['pdgId'] == 22:          continue   # Avoid photon or generator copies of it
      if other['status'] < 0:           continue   # Only final state particles
      if other['pt'] < ptCut:           continue   # pt > 5
      if deltaR( g, other ) > coneSize: continue   # check deltaR
      return False
    return True

# Categories for overlap removal (moved to object selection genPhotonSelector
#def isTTGammaPhoton( g ):
#    return g['pt'] > 13 and abs(g['eta']) < 3.0

#def isZGammaPhoton( g ):
#    return g['pt'] > 15 and abs(g['eta']) < 2.6

#def isIsoTTGammaPhoton( g, genparts ):
#    return g['pt'] > 13 and abs(g['eta']) < 3.0 and isIsolatedPhoton( g, genparts, 0.2 )

#def isIsoZGammaPhoton( g, genparts ):
#    return g['pt'] > 15 and abs(g['eta']) < 2.6 and isIsolatedPhoton( g, genparts, 0.2 )

# Run through parents in genparticles, and return list of their pdgId
def getParentIds( g, genParticles ):
  parents = []

  if g['genPartIdxMother'] > 0:
    try:
        mother1 = genParticles[g['genPartIdxMother']]
        parents += [mother1['pdgId']] + getParentIds( mother1, genParticles )
    except:
        # when no 'status' selection is made for g, this can run in a kind of endless-loop, then python throws an Exception
        return parents
  return parents

def hasMesonMother( parentList ):
    parentList = map( abs, set(parentList) )
    return max(parentList) > 37 if len(parentList)!=0 else False

def getPhotonCategory( g, genparts ):

    # safe time if g is no photon or electron
    if g is None or abs(g['pdgId']) not in [11,22]: return 3

    isIsolated = isIsolatedPhoton( g, genparts, 0.2 )
    hasMeson   = hasMesonMother( getParentIds( g, genparts ) )

    if abs(g['pdgId']) == 22 and isIsolated and not hasMeson: return 0        # type 0: genuine photon:   isolated photon with no meson in parent list
    if abs(g['pdgId']) == 22 and isIsolated and hasMeson:     return 1        # type 1: hadronic photon:  isolated photon with meson in parent list
    if abs(g['pdgId']) == 11 and isIsolated and not hasMeson: return 2        # type 2: miss-Id electron: electron with deltaR and meson-mother requirement from genuine photon
    return 3                                                                  # type 3: none of the above ( e.g. non-isolated )
