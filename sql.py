import psycopg2
import pandas as pd


# Rename this file to sql.py
# Fill in credentials
host='data-analytics-course.c8g8r1deus2v.eu-central-1.rds.amazonaws.com'
port='5432'
database='postgres'
user='danielkwetschas'
password='3asVJlq0Wn7OLcjD'

def get_conn():
    return psycopg2.connect(host=host,
                            port=port,
                            database=database,
                            user=user,
                            password=password)


def get_data(string):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # create a connection to the PostgreSQL server
        conn = get_conn()
                        
        df = pd.read_sql_query(string, con=conn)
	    # close the connection to the PostgreSQL database
        
        conn.close()
        return df
    # the code below makes the function more robust, you can ignore this part
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

## Do NOT change anything below!
# sqlalchemy engine for writing data to a database
from sqlalchemy import create_engine    
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
