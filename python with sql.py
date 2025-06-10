import sqlite3

db = sqlite3.connect('student_db.db')
cursor = db.cursor()

# create new table
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

def menu():
    print("\n Welcome to the superior student managment system!!! \n")
    try:
        choice = int(input("1. Insert a new record \n2. View the database \n3. Update University and course of choice \n4. Update grades \n5. Delete a record \n"))
    except:
        print("Wrong type of input: INVALID")
        choice = int(input("1. Insert a new record \n 2. View the database \n 3. Update University and course of choice \n 4. Update grades \n 5. Delete a record \n"))

    if choice == 1:
        insert()
    elif choice == 2:
        view_data()
    elif choice == 3:
        update_UNI()
    elif choice == 4:
        update_GRADE()
    elif choice == 5:
        delete()

# Inserting record
def insert():
    
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

# View database
def view_data():
    cursor.execute('SELECT * FROM student')
    data = cursor.fetchall()

    for line in data:
        print(line)
    menu()

# Updating record
def update_UNI():
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
 

def update_GRADE():
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
    
    
    
def delete():
    ID = input("Enter the ID of the record you want deleted: ")
    cursor.execute("""
    DELETE FROM student
    WHERE id = ?
    """,(ID))
    db.commit()
    menu

menu()
#close database on script end
db.close()
