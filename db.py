import psycopg2

try:
    connection = psycopg2.connect(user = "reminder",
                                  password = "reminder_pass",
                                  host = "0.0.0.0",
                                  port = "5432",
                                  database = "reminds_db")
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