import sqlite3

def createtable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno  INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

def insert(roll, nam, mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll, nam, mark))
    conn.commit()
    conn.close()

#createtable()
insert(1, 'Apple', 90.00)
def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
print(view())

def delete(roll):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno = ?",(roll,))
    conn.commit()
    conn.close()

#delete(1)

def update(roll, nam, mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE data SET name = ?,marks = ? where rollno = ?",(nam, mark,roll))
    conn.commit()
    conn.close()

update(5, 'Google', 500)

print(view())
