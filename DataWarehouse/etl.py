import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tables(cur, conn):
    """
    this function loads staging tables by reading files from s3
    Args:
       cur -- the cursor class. it allows Python code to execute
              queries against the redshift database
       conn -- connection to redshift database
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    """
    this function populates fact and dimension tables by reading data from staging tables
    Args:
       cur -- the cursor class. it allows Python code to execute
              queries against the redshift database
       conn -- connection to redshift database
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    the main function that builds the ETL pipeline
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()
