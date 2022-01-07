import sqlite3

def connecting():
    con = sqlite3.connect("list_names.db")
    data = con.cursor()
    return con, data

def create():
    con, data = connecting()
    return data.execute("CREATE TABLE column_names (name)")

def clear():
    con, data = connecting()
    data.execute("DELETE FROM column_names")
    con.commit()

def input(name):
    con, data = connecting()
    data.execute("INSERT INTO column_names VALUES (?)", str(name))
    con.commit()

def choice(name):
    con, data = connecting()
    sql = "SELECT * FROM column_names WHERE name = ?"
    data.execute(sql, name)
    res = data.fetchall()
    con.close()
    return res[0][0]

def all_name():
    con, data = connecting()
    sql = "SELECT * FROM column_names"
    data.execute(sql)
    res = data.fetchall()
    con.close()
    return res
