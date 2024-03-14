import psycopg2 as psql
from dotenv import load_dotenv
import os

load_dotenv()


class Database:
    @staticmethod
    def connect(query, typ):
        dbs = psql.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            host=os.getenv('DB_HOST'),
            password=os.getenv('DB_PASSWORD'))

        cursor = dbs.cursor()
        cursor.execute(query)
        if typ == 'insert':
            dbs.commit()
            return 'inserted successful'
        if typ == 'select':
            return cursor.fetchall()
