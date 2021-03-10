import psycopg2

def createtable():
    conn = psycopg2.connect("dbname = 'data2' user = 'postgres' password = 'pm12345' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno  INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

def insert(roll, nam, mark):
    conn = psycopg2.connect("dbname = 'data2' user = 'postgres' password = 'pm12345' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)",(roll, nam, mark))
    conn.commit()
    conn.close()

#createtable()
#insert(1, 'Raj', 90.00)

def view():
    conn = psycopg2.connect("dbname = 'data2' user = 'postgres' password = 'pm12345' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
print(view())

def delete(roll):
    conn = psycopg2.connect("dbname = 'data2' user = 'postgres' password = 'pm12345' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno = %s",(roll,))
    conn.commit()
    conn.close()

#delete(2)

def update(roll, nam, mark):
    conn = psycopg2.connect("dbname = 'data2' user = 'postgres' password = 'pm12345' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name = %s,marks = %s where rollno = %s",(nam, mark,roll))
    conn.commit()
    conn.close()

update(3, 'Ram', 100)

print(view())

# Ref doc : https://docs.python.org/3/library/sqlite3.html
