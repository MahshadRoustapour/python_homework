"""
--I wrote these queries in mysql shell
CREATE DATABASE library_management;

USE library_management;


CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(255)
);


CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    position VARCHAR(100)
);


CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(100),
    publication_year INT,
    genre VARCHAR(50)
);"""


import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='library_management',
            user='root',
            password='mahshad****'
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    except Exception as e:
        print(e)


def register_member(connection, name, email, phone, address):
    cursor = connection.cursor()
    query = """INSERT INTO members (name, email, phone, address) 
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (name, email, phone, address))
    connection.commit()
    print("Member registered successfully")

def remove_member(connection, member_id):
    cursor = connection.cursor()
    query = "DELETE FROM members WHERE member_id = %s"
    cursor.execute(query, (member_id,))
    connection.commit()
    print("Member removed successfully")

def show_member_profile(connection, member_id):
    cursor = connection.cursor()
    query = "SELECT * FROM members WHERE member_id = %s"
    cursor.execute(query, (member_id,))
    result = cursor.fetchone()
    if result:
        print(f"Member ID: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"Email: {result[2]}")
        print(f"Phone: {result[3]}")
        print(f"Address: {result[4]}")
    else:
        print("Member not found.")

def add_employee(connection, name, email, position):
    cursor = connection.cursor()
    query = """INSERT INTO employees (name, email, position) 
               VALUES (%s, %s, %s)"""
    cursor.execute(query, (name, email, position))
    connection.commit()
    print("Employee added successfully")

def show_employee_details(connection, employee_id):
    cursor = connection.cursor()
    query = "SELECT * FROM employees WHERE employee_id = %s"
    cursor.execute(query, (employee_id,))
    result = cursor.fetchone()
    if result:
        print(f"Employee ID: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"Email: {result[2]}")
        print(f"Position: {result[3]}")
    else:
        print("Employee not found")

def add_book(connection, title, author, publication_year, genre):
    cursor = connection.cursor()
    query = """INSERT INTO books (title, author, publication_year, genre) 
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (title, author, publication_year, genre))
    connection.commit()
    print("Book added successfully")

def update_book_info(connection, book_id, title=None, author=None, publication_year=None, genre=None):
    cursor = connection.cursor()
    query = "UPDATE books SET title = %s, author = %s, publication_year = %s, genre = %s WHERE book_id = %s"
    cursor.execute(query, (title, author, publication_year, genre, book_id))
    connection.commit()
    print("Book information updated successfully")

def search_books_by_title(connection, title):
    cursor = connection.cursor()
    query = "SELECT * FROM books WHERE title LIKE %s"
    cursor.execute(query, ('%' + title + '%',))
    result = cursor.fetchall()
    if result:
        for book in result:
            print(f"Book ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Year: {book[3]}")
            print(f"Genre: {book[4]}")
    else:
        print("No books found with that title")

def main():
    connection = create_connection()
    
    while True:
        print("\nLibrary Management System")
        print("1. Register Member")
        print("2. Remove Member")
        print("3. Show Member Profile")
        print("4. Add Employee")
        print("5. Show Employee Details")
        print("6. Add Book")
        print("7. Update Book Info")
        print("8. Search Books by Title")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            phone = input("Enter member phone: ")
            address = input("Enter member address: ")
            register_member(connection, name, email, phone, address)
        
        elif choice == 2:
            member_id = int(input("Enter member ID to remove: "))
            remove_member(connection, member_id)
        
        elif choice == 3:
            member_id = int(input("Enter member ID to show profile: "))
            show_member_profile(connection, member_id)
        
        elif choice == 4:
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            position = input("Enter employee position: ")
            add_employee(connection, name, email, position)
        
        elif choice == 5:
            employee_id = int(input("Enter employee ID to show details: "))
            show_employee_details(connection, employee_id)
        
        elif choice == 6:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = int(input("Enter publication year: "))
            genre = input("Enter book genre: ")
            add_book(connection, title, author, publication_year, genre)
        
        elif choice == 7:
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title (leave blank to skip): ")
            author = input("Enter new author (leave blank to skip): ")
            publication_year = input("Enter new publication year (leave blank to skip): ")
            genre = input("Enter new genre (leave blank to skip): ")
            update_book_info(connection, book_id, title or None, author or None, publication_year or None, genre or None)
        
        elif choice == 8:
            title = input("Enter title to search: ")
            search_books_by_title(connection, title)
        
        elif choice == 9:
            print("Exiting the system")
            break
        
        else:
            print("Please try again")


if __name__ == "__main__":
    main()