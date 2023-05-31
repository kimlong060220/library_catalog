import mysql.connector


mydb = mysql.connector.connect(
            host='localhost',
            user='longlk',
            password='@Log0602',
            database='library_catalog'
        )
cursor = mydb.cursor()

query = """
        SELECT * FROM books;
        """
cursor.execute(query)
print(cursor.fetchall())