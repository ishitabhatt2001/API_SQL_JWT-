import psycopg2


def establish_database_connection():

    conn=psycopg2.connect(host="localhost" ,port=5432 ,database="postgres" , user="postgres" , password="suraasa")
    cursor = conn.cursor()
    return conn,cursor


