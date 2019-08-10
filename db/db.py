import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


try:
    connection = psycopg2.connect(user = os.environ.get("DB_USER"),
                                  password = os.environ.get("DB_PASSWORD"),
                                  host = os.environ.get("DB_HOST"),
                                  port = os.environ.get("DB_PORT"),
                                  database = os.environ.get("DB_NAME"))
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE IF NOT EXISTS reminds
    (ID SERIAL PRIMARY KEY     NOT NULL,
    DAY_REMIND           VARCHAR(8)    NOT NULL,
    TIME_REMIND         VARCHAR(5) NOT NULL,
    REMIND_TEXT         TEXT NOT NULL
    STATUS    BOOLEAN NOT NULL); '''

    cursor.execute(create_table_query)

    insert_remind('12.03', '13:00', 'first reminder')
    
    get_remind()
    connection.commit()
    print("Table created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insert_remind(date, time, remind):
    try:
    
        sql = """ INSERT INTO reminds (DAY_REMIND, TIME_REMIND, REMIND_TEXT) VALUES (%s, %s, %s) """
        data = (date, time, remind)
        cursor.execute(sql, data)

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into reminds table", error)


def get_remind():
    try:
    
        sql = """ SELECT * FROM reminds """
        cursor.execute(sql)

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to SELECT records into reminds table", error)