import os
import pandas as pd
import utils

BASE_DIR  = os.path.dirname( os.path.dirname ( os.path.dirname( os.path.dirname(__file__) ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data')
SQL_DIR = os.path.join( BASE_DIR, 'src', 'sql')

conn = utils.connect_db()

query = utils.import_query(os.path.join( SQL_DIR, 'lifetime.sql'))

df = pd.read_sql_query(query, conn)

df.to_csv(os.path.join(DATA_DIR, 'lifetime.csv'), sep=';', index=False)
