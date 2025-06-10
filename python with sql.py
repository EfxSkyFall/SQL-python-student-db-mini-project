import sqlite3

db = sqlite3.connect('student_db.db')
cursor = db.cursor()

#Create new table - Checking if a table called student exists, if not a table is created.
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    choice TEXT NOT NULL,
    grade1 TEXT NOT NULL,
    grade2 TEXT NOT NULL,
    grade3 TEXT NOT NULL
);
''')

db.commit()
#Menu - The general menu, appears after each opearation, used for navigation.
def menu():
    print("\n Welcome to the superior student managment system!!! \n")
    try:
        choice = int(input("\n1. Insert a new record \n2. View the database \n3. Update University and course of choice \n4. Update grades \n5. Delete a record \n6. Exit \n"))
    except:
        print("Wrong type of input: INVALID")
        choice = int(input("\n1. Insert a new record \n 2. View the database \n 3. Update University and course of choice \n 4. Update grades \n 5. Delete a record \n6. Exit \n"))

    if choice == 1:
        insert_record()
    elif choice == 2:
        view_data()
    elif choice == 3:
        update_UNI()
    elif choice == 4:
        update_GRADE()
    elif choice == 5:
        delete_record()
    elif choice == 6:
        print("Thank you for using my python database managment system")
        pass
    

#Inserting record - entering a new record into the table.
def insert_record():
    
    name = input('Enter Name: ')
    course = input('Enter the university course you are applying for: ')
    choice = input('Enter your first choice University: ')
    grade1 = input("Enter grade of subject 1: ")
    grade2 = input("Enter grade of subject 2: ")
    grade3 = input("Enter grade of subject 3: ")

    cursor.execute('''
    INSERT INTO student (name,course,choice,grade1,grade2,grade3)
    VALUES
        (?,?,?,?,?,?)
    ''',(name,course,choice,grade1,grade2,grade3))

    db.commit()
    menu()

#View database - displaying the current records in the database.
def view_data():
    cursor.execute('SELECT * FROM student')
    data = cursor.fetchall()

    for line in data:
        print(line)
    menu()

#Updating record - Changing the university and course of the specified ID number.
def update_UNI():
    try:
        ID = input("Enter your ID: ")
    except:
        print("Wrong type of input: INVALID")
        ID = input("Enter your ID: ")
        
    nchoice = input("Enter your new University Choice: ")
    ncourse = input("Enter your new course choice at "+nchoice+": ")
    
    cursor.execute('''
    UPDATE student
    SET course = ?, choice = ?
    WHERE id = ?
    ''',(ncourse,nchoice,ID))
    db.commit()
    menu()
 
#Updating record - Changing the grades of a specified ID number.
def update_GRADE():
    try:
        ID = input("Enter your ID: ")
    except:
        print("Wrong type of input: INVALID")
        ID = input("Enter your ID: ")
    ngrade1 = input("Renter grade of subject 1: ")
    ngrade2 = input("Renter grade of subject 2: ")
    ngrade3 = input("Renter grade of subject 3: ")

    cursor.execute('''
    UPDATE student
    SET grade1 = ?, grade2 = ?, grade3 = ?
    WHERE id = ?
    ''',(ngrade1,ngrade2,ngrade3,ID))
    db.commit()
    menu()
    
    
#Deleting a record - removes a record from the table.   
def delete_record():
    try:
        ID = input("Enter the ID of the record you want deleted: ")
    except:
        print("Wrong type of input: INVALID")
        ID = input("Enter the ID of the record you want to be deleted: ")
        
    cursor.execute("""
    DELETE FROM student
    WHERE id = ?
    """,(ID))
    db.commit()
    menu()

menu()
#Closes the database on script end.
db.close()
