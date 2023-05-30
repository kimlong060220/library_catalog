import mysql.connector
from typing import List
from schema import BookCreate, BookUpdate, MemberCreate, MemberUpdate


class LibraryService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="longlk",
            password="@Log0602",
        )
        self.cursor = self.connection.cursor()
        self.create_database()
        self.cursor.execute("USE library_catalog")
        self.create_tables()

    def create_database(self):
        self.cursor.execute("DROP DATABASE IF EXISTS library_catalog")
        self.cursor.execute("CREATE DATABASE library_catalog")
        self.connection.commit()

    def create_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS books")
        self.cursor.execute("DROP TABLE IF EXISTS members")
        self.cursor.execute("DROP TABLE IF EXISTS book_borrowals")

        self.cursor.execute(
            """
            CREATE TABLE books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                publication_year INT NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS members (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                membership_id INT NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS book_borrowals (
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_id INT NOT NULL,
                member_id INT NOT NULL,
                borrow_date DATE NOT NULL,
                return_date DATE,
                FOREIGN KEY (book_id) REFERENCES books (id),
                FOREIGN KEY (member_id) REFERENCES members (id)
            )
            """
        )
        self.connection.commit()
    def create_book(self, book: BookCreate) -> BookCreate:
        query = "INSERT INTO books (title, author, publication_year) VALUES (%s, %s, %s)"
        values = (book.title, book.author, book.publication_year)
        self.cursor.execute(query, values)
        self.connection.commit()
        book_id = self.cursor.lastrowid
        return BookCreate(**book.dict(), id=book_id)

    def get_book(self, book_id: int) -> BookCreate:
        query = "SELECT * FROM books WHERE id = %s"
        self.cursor.execute(query, (book_id,))
        result = self.cursor.fetchone()
        if result:
            book = BookCreate(id=result[0], title=result[1], author=result[2], publication_year=result[3])
            return book
        return None

    def update_book(self, book_id: int, book: BookUpdate) -> BookCreate:
        existing_book = self.get_book(book_id)
        if not existing_book:
            return None

        query = "UPDATE books SET title = %s, author = %s, publication_year = %s WHERE id = %s"
        values = (book.title, book.author, book.publication_year, book_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        return BookCreate(**book.dict(), id=book_id)

    def get_all_books(self) -> List[BookCreate]:
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        books = []
        for result in results:
            book = BookCreate(id=result[0], title=result[1], author=result[2], publication_year=result[3])
            books.append(book)
        return books

    def create_member(self, member: MemberCreate) -> MemberCreate:
        query = "INSERT INTO members (name, membership_id) VALUES (%s, %s)"
        values = (member.name, member.membership_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        member_id = self.cursor.lastrowid
        return MemberCreate(**member.dict(), id=member_id)

    def get_member(self, member_id: int) -> MemberCreate:
        query = "SELECT * FROM members WHERE id = %s"
        self.cursor.execute(query, (member_id,))
        result = self.cursor.fetchone()
        if result:
            member = MemberCreate(id=result[0], name=result[1], membership_id=result[2])
            return member
        return None

    def update_member(self, member_id: int, member: MemberUpdate) -> MemberCreate:
        existing_member = self.get_member(member_id)
        if not existing_member:
            return None

        query = "UPDATE members SET name = %s, membership_id = %s WHERE id = %s"
        values = (member.name, member.membership_id, member_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        return MemberCreate(**member.dict(), id=member_id)

    def get_all_members(self) -> List[MemberCreate]:
        query = "SELECT * FROM members"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        members = []
        for result in results:
            member = MemberCreate(id=result[0], name=result[1], membership_id=result[2])
            members.append(member)
        return members
