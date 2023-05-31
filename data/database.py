import mysql.connector
import icecream as ic

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='longlk',
            password='@Log0602'
        )
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):
        with open("data/create_tables.sql", 'r') as file:
            queries = file.read().split(';')[:-1]
            for query in queries:
                if query:
                    self.cursor.execute(query)
        self.conn.commit()

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        cursor.execute(query, params)

        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            self.conn.commit()
            cursor.close()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

db = Database()
query = "SELECT * FROM ratings WHERE book_id = %s"
params = (3,)
ratings = db.execute_query(query, params)
print(ratings)