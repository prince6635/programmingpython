"""
Avoid limitations to save data in files - pickle module
The pickle module translates an in-memory Python object into a serialized byte stream a string of bytes
that can be written to any file-like object. The pickle module also knows how to re-construct the original object in memory,
given the serialized byte stream: we get back the exact same object.
In a sense, the pickle module replaces proprietary data formats
its serialized format is general and efficient enough for any program.
With pickle, there is no need to manually translate objects to data when storing them persistently,
and no need to manually parse a complex format to get them back.
Pickling is similar in spirit to XML representations
"""

from initdata import db
from util import generatePathUnderDataFolder
import pickle

DEFAULT_PICKLE_FILENAME = generatePathUnderDataFolder('people-pickle')

def storeDbase(dbfilename=DEFAULT_PICKLE_FILENAME):
    dbfile = open(dbfilename, 'wb')
    pickle.dump(db, dbfile)
    dbfile.close()

def loadDbase(dbfilename=DEFAULT_PICKLE_FILENAME):
    dbfile = open(dbfilename, 'rb')
    db = pickle.load(dbfile)
    dbfile.close()
    for key in db:
        print(key, '=>\n ', db[key])
    print(db['sue']['name'])
    return db

def updateDbase(dbfilename=DEFAULT_PICKLE_FILENAME):
    db = loadDbase(dbfilename)
    db['sue']['pay'] *= 1.10
    db['tom']['name'] = 'Tom Tom'

    dbfile = open(dbfilename, 'wb')
    pickle.dump(db, dbfile)
    dbfile.close()


