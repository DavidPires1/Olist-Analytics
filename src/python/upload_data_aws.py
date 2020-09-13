import os
import pandas as pd
import sqlalchemy


user = 'twitch' #login
psw = 'teodoroc' #senha
host = 'olistmysql.cqpgtc5jemwi.us-east-2.rds.amazonaws.com' #ip/host/dns
port ='3306' #port quem passa isso é a TI


str_connection = 'mysql+pymysql://{user}:{psw}@{host}:{port}'

BASE_DIR = os.path.dirname( os.path.dirname ( os.path.abspath(__file__) ) )
DATA_DIR = os.path.join ( BASE_DIR, 'data' )


files_names = [i for i in os.listdir( DATA_DIR ) if i.endswith('.csv')]

str_connection = str_connection.format( user=user, psw=psw, host=host, port=port )
connection = sqlalchemy.create_engine( str_connection )

for i in files_names:
    df_tmp = pd.read_csv( os.path.join( DATA_DIR, i ) )
    table_name = "tb_" + i.strip(".csv").replace("olist_","").replace("_dataset","")
    df_tmp.to_sql( table_name, 
                    connection, 
                    schema='Olist',
                    if_exists='replace',
                    index=False
                    )