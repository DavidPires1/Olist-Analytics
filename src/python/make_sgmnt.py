import os
import sqlalchemy
import argparse
import pandas as pd

import sqlite3
import utils



#Os endereços do nosso projeto e sub pastas
BASE_DIR  = os.path.dirname( os.path.dirname ( os.path.dirname( os.path.dirname(__file__) ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data')
SQL_DIR = os.path.join( BASE_DIR, 'src', 'sql')


# Parser de data para fazer foto
parser = argparse.ArgumentParser()
parser.add_argument( '--date_end', '-e', help='Data de fim da extração', default = '2018-06-01')
args = parser.parse_args()

date_end = args.date_end
ano = int(date_end.split('-')[0]) -1
mes = int(date_end.split('-')[1])
date_init = f'{ano}-{mes}-01'

# Importa a query
query = utils.import_query(os.path.join( SQL_DIR, 'segmentos.sql'))
query = query.format( date_init = date_init,
                     date_end = date_end )

# Abrindo conexão com banco...
conn = utils.connect_db()

create_query = f'''
CREATE TABLE tb_sellers_sgmnt AS
{query}
;'''

insert_query = f'''
DELETE FROM tb_sellers_sgmnt WHERE DT_SGMNT = '{date_end}';
INSERT INTO tb_sellers_sgmnt
{query}
;'''

try:
    utils.execute_many_sql( create_query, conn)
except:
    utils.execute_many_sql( insert_query, conn, verbose=True)
