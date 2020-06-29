import pandas as pd
from config import DB_DETAILS
import mysql.connector as mc
import psycopg2 as pg
from mysql.connector import errorcode as ec


def load_db_details(env):
    return DB_DETAILS[env]


def get_mysql_connection(host, db, user, password):

    try:
        connection = mc.connect(host=host,
                                database=db,
                                user=user,
                                password=password
                                )
        return connection
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print(error)


def get_pg_connection(host, db, user, password):
    connection = pg.connect(host=host,
                            database=db,
                            user=user,
                            password=password
                            )
    return connection



def get_connection(db_type, db_host, db_name, db_user, db_pass):
    conn = None
    if db_type == 'mysql':
        conn = get_mysql_connection(host=db_host, db=db_name, user=db_user, password=db_pass)

    if db_type == 'postgres':
        conn = get_pg_connection(host=db_host, db=db_name, user=db_user, password=db_pass)

    return conn



def get_tables(path, table_list):
    tables = pd.read_csv(path, sep=':')
    if table_list == 'all':
        return tables.query('to_be_loaded == "yes"')
    else:
        table_list_df = pd.DataFrame(table_list.split(','), columns=['table_name'])
        return tables.join(table_list_df.set_index('table_name'), on='table_name', how='inner'). \
            query('to_be_loaded == "yes"')
