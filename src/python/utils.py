import pandas as pd
import os
import sqlalchemy
from tqdm import tqdm

BASE_DIR  = os.path.dirname( os.path.dirname ( os.path.dirname( os.path.abspath(__file__) ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data')
DB_PATH = os.path.join( DATA_DIR, 'olist.db')


def import_query(path, **kwargs):
    """ Essa função realiza o import de uma query onde pode ser passado vários argumentos de import (read()) """
    with open( path, 'r', **kwargs ) as files_query:
        query = files_query.read()
    return query

def connect_db():
    """ Função para conectar ao bando de dados local (sqlite) """
    str_connection = 'sqlite:///{path}'.format(path=DB_PATH)
    connection = sqlalchemy.create_engine( str_connection )
    return connection

def execute_many_sql( sql, conn, verbose = False):
    if verbose:
        for i in tqdm(sql.split(';')[:-1]):
            conn.execute( i )
    else:
        for i in sql.split(';')[:-1]:
            conn.execute( i )
    



