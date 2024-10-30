import psycopg2
from config import config

def connect():
    conn = None
    try:
        params =config()
        conn = psycopg2.connect(**params)
        # print("Connected to the Database Succesfully")
        return conn
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
