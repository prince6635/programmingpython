from step2_lib import dump_db_file
from step2_lib import initdata
from step2_lib import make_db_file
from step2_lib import update_db_file
from step2_lib import make_db_pickle
from step2_lib import make_db_pickle_file_per_record
from step2_lib import make_db_shelve

print("regular save to files")
make_db_file.storeDbase(initdata.db)
dump_db_file.dumpDbFile()

update_db_file.updateDbase()
dump_db_file.dumpDbFile()
print("======================")

print("save to files with pickle module")
make_db_pickle.storeDbase()
make_db_pickle.loadDbase()
make_db_pickle.updateDbase()
make_db_pickle.loadDbase()
print("======================")

print("save each record into a seperate file")
make_db_pickle_file_per_record.storeDbase()
make_db_pickle_file_per_record.loadDbase()

make_db_pickle_file_per_record.updateDbase()
make_db_pickle_file_per_record.loadDbase()
print("======================")

print("use shelve to replace pickle for record-each-file")
make_db_shelve.storeDbase()
make_db_shelve.loadDbase()

make_db_shelve.updateDbase()
make_db_shelve.loadDbase()
print("======================")

