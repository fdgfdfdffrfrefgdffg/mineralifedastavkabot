from sqlite3 import Connection

conn = Connection("data.db")
c = conn.cursor()

def default():
    c.execute("CREATE TABLE IF NOT EXISTS users(id, login, parol)")
    conn.commit()

def add_user(id, login, parol):
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (id, login, parol))
    conn.commit()

def get_user(id):
    return c.execute("SELECT * FROM users WHERE id=?", (id, )).fetchone()


def close_db():
    conn.close()

default()



