from pathlib import Path
from creating_db_functions import create_groups_table
from write_db_functions import write_groups

test_db = 'test_db_2.db'

create_groups_table(test_db)

muz_1 = '/media/kwenus/kwenus I/MUZ/1/'
muz_2 =  '/media/kwenus/kwenus I/MUZ/2/'

muzlib_source = Path(muz_1)

folders_data = []

for folder in muzlib_source.iterdir():
    folders_data.append((str(folder.name), str(folder.resolve())))

write_groups(test_db, folders_data)


