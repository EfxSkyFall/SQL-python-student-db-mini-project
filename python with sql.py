import sqlite3

db = sqlite3.connect('student_db.db')
cursor = db.cursor()

# create new table
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    grade1 TEXT NOT NULL,
    grade2 TEXT NOT NULL,
    grade3 TEXT NOT NULL
);
''')

db.commit()

# inserting record
name = input('Enter Name: ')
course = input('Enter the university course you are applying for: ')
grade1 = input("Enter grade of subject 1: ")
grade2 = input("Enter grade of subject 2: ")
grade3 = input("Enter grade of subject 3: ")

cursor.execute('''
INSERT INTO student (name,course,grade1,grade2,grade3)
VALUES
    (?,?,?,?,?)
''',(name,course,grade1,grade2,grade3))

db.commit()

#VIEW database
cursor.execute('SELECT * FROM student')
data = cur.fetchall()

for line in data:
    print(line)

# updating record
curosr.execute('''
UPDATE student
SET
''')



#close database on script end
db.close()
