import sqlite3

conn = sqlite3.connect('data.db')


def create():
    conn.execute('''CREATE TABLE IF NOT EXISTS Admins(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT NOT NULL,
    AdminLevel TEXT NOT NULL)''')


def insert(name, roll):
    conn.execute(
        "INSERT INTO Admins(USERNAME,AdminLevel) VALUES(?,?)", (name, roll))
    conn.commit()


def read():
    data = conn.execute(
        "SELECT ID, USERNAME,AdminLevel FROM Admins /**WHERE ID=1 **/")
    for i in data:
        if "Sannidhya Dasgupta" in i:
            print("Sannndihya is there")
        else:
            print("Not there")


def update(new, sno):
    # cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sql_update_query = """Update Admins set USERNAME = ? where id = ?"""
    data = (new, sno)
    # .execute(sql_update_query, data)
    conn.execute(sql_update_query, data)
    conn.commit()
    print("Record Updated successfully")
    # cursor.close()


def delete(sno):
    sql = 'DELETE FROM tasks WHERE id=?'
    conn.execute(sql, sno)
    print("Deleted")


if __name__ == "__main__":
    # update("Haris Ali Khan", 1)
    # create()
    read()
    # update("Sannidhya Dasgupta", "2")
    conn.close()
