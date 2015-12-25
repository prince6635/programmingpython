from __future__ import print_function # enable the Python 3 syntax if you are using Python 2.6 or 2.7

from PartI_SampleProject.util import generatePathUnderDataFolder

"""
Save in-memory database object to a file with custom formatting;
assume 'endrec.', 'enddb.', and '=>' are not used in the data;
assume db is dict of dict;
warning: eval can be dangerous - it runs strings as code;
could also eval() record dict all at once;
could also dbfile.write(key + '\n') vs print(key, file=dbfile); """

DEFAULT_DB_FILENAME = generatePathUnderDataFolder('people-file')
END_DB = 'enddb.'
END_REC = 'endrec.'
REC_SEP = '=>'

def storeDbase(db, dbfilename=DEFAULT_DB_FILENAME):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + REC_SEP + repr(value), file=dbfile)
        print(END_REC, file=dbfile)
    print(END_DB, file=dbfile)
    dbfile.close()

def loadDbase(dbfilename=DEFAULT_DB_FILENAME):
    "parse data to reconstruct database"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    # For Python 2, use raw_input() instead of input()
    key = raw_input()
    while key != END_DB:
        rec = {}
        field = raw_input()
        while field != END_REC:
            name, value = field.split(REC_SEP)
            rec[name] = eval(value)
            field = raw_input()
        db[key] = rec
        key = raw_input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDbase(db)


