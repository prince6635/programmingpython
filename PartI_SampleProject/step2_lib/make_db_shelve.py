"""
Python module to replace make_db_pickle_file_per_record.py:
Shelves automatically pickle objects to and from a keyed-access filesystem.
They behave much like dictionaries that must be opened, and they persist after each program exits.
Because they give us key-based access to stored records,
there is no need to manually manage one flat file per record, the shelve system automatically
splits up stored re-cords and fetches and updates only those records that are accessed and changed.
In this way, shelves provide utility similar to per-record pickle files, but they are usually easier to code.
"""

import initdata
import shelve

from util import generatePathUnderDataFolder

DEFAULT_FILE_NAME = generatePathUnderDataFolder('people-shelve')

def storeDbase():
    db = shelve.open(DEFAULT_FILE_NAME)
    db['bob'] = initdata.bob
    db['sue'] = initdata.sue
    db.close()

def loadDbase():
    db = shelve.open(DEFAULT_FILE_NAME)
    for key in db:
        print(key, '=>\n ', db[key])
    print(db['sue']['name'])
    db.close()
    return db

def updateDbase():
    db = shelve.open(DEFAULT_FILE_NAME)
    sue = db['sue']
    sue['pay'] *= 1.10
    db['sue'] = sue
    db['tom'] = initdata.tom
    db.close()



