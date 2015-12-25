"""
Disadvantage of saving the whole db in one file:
it may become slow for very large databases:
because the entire database must be loaded and rewritten to update a single record,
We could improve on this by storing each record in the database in a separate flat file.
using each record's original key as its filename with a .pkl appended
(it creates the files bob.pkl, sue.pkl, and tom.pkl in the current working directory).
"""

import glob
import pickle

import initdata
from PartI_SampleProject.util import generatePathUnderDataFolder


def storeDbase():
    for (key, record) in [('bob', initdata.bob), ('tom', initdata.tom), ('sue', initdata.sue)]:
        recordFile = open(generatePathUnderDataFolder(key + '.pkl'), 'wb')
        pickle.dump(record, recordFile)
        recordFile.close()

def loadDbase():
    for fileName in glob.glob('*.pkl'):
        recFile = open(fileName, 'rb')
        record = pickle.load(recFile)
        print(fileName, '=>\n ', record)
    sueFile = open(generatePathUnderDataFolder('sue.pkl'), 'rb')
    print(pickle.load(sueFile))

def updateDbase():
    sueFile = open(generatePathUnderDataFolder('sue.pkl'), 'rb')
    sue = pickle.load(sueFile)
    sueFile.close()

    sue['pay'] *= 1.10
    sueFile = open(generatePathUnderDataFolder('sue.pkl'), 'wb')
    pickle.dump(sue, sueFile)
    sueFile.close()