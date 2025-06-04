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
        (?,?,?,?,?)
    ''',(name,course,choice,grade1,grade2,grade3))

    db.commit()

# View database
def view_data():
    cursor.execute('SELECT * FROM student')
    data = cur.fetchall()

    for line in data:
        print(line)

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
 

def update_GRADE():
    pass
    
update_UNI()


#close database on script end
db.close()
