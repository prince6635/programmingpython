from make_db_file import loadDbase

def dumpDbFile():
    db = loadDbase()
    for key in db:
        print(key, '=>\n ', db[key])
    print(db['sue']['name'])
