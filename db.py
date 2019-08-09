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
    create_table_query = '''CREATE TABLE reminds
    (ID INT PRIMARY KEY     NOT NULL,
    DAY_REMIND           DATE    NOT NULL,
    TIME_REMIND         TIME NOT NULL,
    REMIND_TEXT         TEXT NOT NULL); '''

    cursor.execute(create_table_query)
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