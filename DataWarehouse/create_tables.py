import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def drop_tables(cur, conn):
    """
    drops all the tables defined in "drop_table_queries" query list
    Args:
        cur: the cursor class. it allows Python code to execute
             queries against the redshift database
        conn: connection to redshift database
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    """
    creates all the tables defined in "create_table_queries" query list
    Args:
        cur: the cursor class. it allows Python code to execute
             queries against the redshift database
        conn: connection to redshift database
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    connects to database specified in the config file,
    drops and creates staging, fact and dimension tables
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()
