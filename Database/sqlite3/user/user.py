import sqlite3
from contextlib import closing
from pprint import pprint


if __name__ == '__main__':
    with closing(sqlite3.connect("user.db3")) as connection:
        with closing(connection.cursor()) as cursor:
            print("Version:", sqlite3.version)
            cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

            cursor.execute("INSERT INTO user (name, email) VALUES (?, ?)", ('John Doe', 'john.doe@example.com'))
            # cursor.execute("INSERT INTO user (name, email) VALUES ('Jane Smith', 'jane.smith@example.com')")
            # cursor.execute("INSERT INTO user (name, email) VALUES ('Dave Johnson', 'dave.johnson@example.com')")
            data = [
                ('John Doe', 'john.doe@example.com'),
                ('Jane Smith', 'jane.smith@example.com'),
                ('Dave Johnson', 'dave.johnson@example.com')
            ]
            cursor.executemany("INSERT INTO user (name, email) VALUES (?, ?)", data)

            pprint(cursor.execute("SELECT * FROM user").fetchall())
            cursor.execute("UPDATE user SET email = 'john.doe@bettermail.com' WHERE name = 'John Doe'")
            pprint(cursor.execute("SELECT * FROM user").fetchall())

            # Needs to be used before creating the cursor
            # connection.row_factory = sqlite3.Row
            # rows = cursor.execute("SELECT * FROM user").fetchall()
            # for row in rows:
            #     pprint(dict(row))

            # connection.commit() # If you want to commit the changes
