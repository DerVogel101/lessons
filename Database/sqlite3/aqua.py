import sqlite3
from contextlib import closing

with closing(sqlite3.connect("aquarium.db")) as connection:
    with closing(connection.cursor()) as cursor:
        print(connection.total_changes)

        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS fish (name TEXT, species TEXT, tank_number INTEGER)")

        cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
        cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

        rows = cursor.execute("SELECT * FROM fish")
        print(rows.fetchall())

        rows = cursor.execute("SELECT name, species, tank_number FROM fish")
        print(rows.fetchall())

        target_fish_name = "Jamie"
        rows = cursor.execute(
            "SELECT name, species, tank_number FROM fish WHERE name = ?",
            (target_fish_name,),
        ).fetchall()
        print(rows)

        # DO NOT USE python string formatting to insert values into SQL queries
        new_tank_number = 2
        moved_fish_name = "Sammy"
        cursor.execute(
            "UPDATE fish SET tank_number = ? WHERE name = ?",
            (new_tank_number, moved_fish_name)
        )

        rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
        print(rows)

        released_fish_name = "Sammy"
        cursor.execute(
            "DELETE FROM fish WHERE name = ?",
            (released_fish_name,)
        )

        rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
        print(rows)

