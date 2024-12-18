import pymongo
from pymongo import MongoClient
from pprint import pprint

def connect_to_mongo():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['student_records_db']
    collection = db['students']
    return collection

def add_student(collection, student_id, name, age):
    student = {
        'student_id': student_id,
        'name': name,
        'age': age
    }
    try:
        result = collection.insert_one(student)
        print(f"Student {name} added with student_id {student_id}.")
    except Exception as e:
        print(e)

def remove_student(collection, student_id):
    try:
        result = collection.delete_one({'student_id': student_id})
        if result.deleted_count > 0:
            print(f"Student with student_id {student_id} has been removed.")
        else:
            print(f"No student found with student_id {student_id}!")
    except Exception as e:
        print(e)

def search_student(collection, student_id):
    try:
        student = collection.find_one({'student_id': student_id})
        if student:
            pprint(student)
        else:
            print(f"No student found with student_id {student_id}.")
    except Exception as e:
        print(e)

def display_students(collection):
    try:
        students = collection.find()
        for student in students:
            pprint(student)
    except Exception as e:
        print(e)

def main():
    collection = connect_to_mongo()

    while True:
        print("1. Add Student Record")
        print("2. Remove Student Record")
        print("3. Search for Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student_id: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            add_student(collection, student_id, name, age)
        elif choice == '2':
            student_id = input("Enter student_id to remove: ")
            remove_student(collection, student_id)
        elif choice == '3':
            student_id = input("Enter student_id to search: ")
            search_student(collection, student_id)
        elif choice == '4':
            display_students(collection)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()