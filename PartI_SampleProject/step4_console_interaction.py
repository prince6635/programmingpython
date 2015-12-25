import shelve
from step3_lib.person import Person
from util import generatePathUnderDataFolder
from step3_lib.make_db_classes import loadDbase

DEFAULT_DB_FILE_NAME = generatePathUnderDataFolder('class-shelve')
fieldNames = ('name', 'age', 'job', 'pay')

# query
def queryInConsole():
    db = shelve.open(DEFAULT_DB_FILE_NAME)
    maxField = max(len(f) for f in fieldNames)

    while True:
        key = raw_input('\nkey? => ')
        if not key:
            break

        try:
            record = db[key]
        except:
            print('No such key "%s"!' % key)
        else:
            for field in fieldNames:
                print(field.ljust(maxField), '=>', getattr(record, field))
    db.close()

# update
def updateInConsole():
    db = shelve.open(DEFAULT_DB_FILE_NAME)
    while True:
        key = raw_input('\nkey? => ')
        if not key:
            break
        if key in db:
            record = db[key]
        else:
            record = Person(name='?', age='?')

        for field in fieldNames:
            curVal = getattr(record, field)
            newVal = raw_input('\t[%s]=%s\n\t\tnew?=>' % (field, curVal))
            if newVal:
                setattr(record, field, newVal)
        db[key] = record
    db.close()


# queryInConsole()

# loadDbase()
# updateInConsole()
# loadDbase()
