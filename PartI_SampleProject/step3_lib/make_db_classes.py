import shelve
from person import Person
from manager import Manager
from PartI_SampleProject.util import generatePathUnderDataFolder

DEFAULT_DB_FILE_NAME = generatePathUnderDataFolder('class-shelve')

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tome Doe', 50, 50000)

def storeDbase():
    db = shelve.open(DEFAULT_DB_FILE_NAME)
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()

def loadDbase():
    db = shelve.open(DEFAULT_DB_FILE_NAME)
    for key in db:
        print(key, '=>\n ', db[key].name, db[key].pay)

    bob = db['bob']
    print(bob.lastName())
    print(db['tom'].lastName())

def updateDbase():
    db = shelve.open(DEFAULT_DB_FILE_NAME)
    sue = db['sue']
    sue.giveRaise(.25)
    db['sue'] = sue

    tom = db['tom']
    tom.giveRaise(.20)
    db['tom'] = tom
    db.close()
