import sqlite3

config = {
    "token": "0"

}
def autosetting():
    with sqlite3.connect('database.db') as connect:
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    score INTEGER NOT NULL,
                    money INTEGER NOT NULL
                    )""")
        connect.commit()