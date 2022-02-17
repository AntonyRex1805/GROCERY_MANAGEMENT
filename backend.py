import sqlite3

def connect():
    conn=sqlite3.connect("grocerylist.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book1 (id integer primary key, SNo text, Product text, MRP integer, Quantity integer)")
    conn.commit()
    conn.close()

def insert(SNo,Product,MRP,Quantity):
    conn=sqlite3.connect("grocerylist.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book1 VALUES (NULL,?,?,?,?)",(SNo,Product,MRP,Quantity))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("grocerylist.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book1")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(SNo="",Product="",MRP="",Quantity=""):
    conn=sqlite3.connect("grocerylist.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book1 WHERE SNo=? OR Product=? OR MRP=? OR Quantity=?", (SNo,Product,MRP,Quantity))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("grocerylist.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book1 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,SNo,Product,MRP,Quantity):
    conn=sqlite3.connect("grocerylist.db")
    cur=conn.cursor()
    cur.execute("UPDATE book1 SET SNo=?, Product=?, MRP=?, Quantity=? WHERE id=?",(SNo,Product,MRP,Quantity,id))
    conn.commit()
    conn.close()

connect()
