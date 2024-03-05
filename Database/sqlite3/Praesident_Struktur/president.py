import sqlite3
from contextlib import closing
from pprint import pprint

with closing(sqlite3.connect("president.db3")) as connection:
    with closing(connection.cursor()) as cursor:
        # Get all presidents ordered by death
        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY death DESC").fetchall())

        # Filter by state VA and order by death and fetch all presidents names
        # pprint(cursor.execute("SELECT first_name, last_name FROM president WHERE state = 'VA' ORDER BY death DESC").fetchall())

        # Filter by state VA and order by death and fetch all presidents names
        # pprint(cursor.execute("SELECT first_name, last_name FROM president WHERE state LIKE 'VA' ORDER BY death DESC").fetchall())

        # Filter by state VA and birth lower than 1750-01-01, order by death and fetch all presidents names
        # pprint(cursor.execute("SELECT first_name, last_name FROM president WHERE state = 'VA' AND birth < '1750-01-01' ORDER BY death DESC").fetchall())

        # Fetch all Living presidents names
        # pprint(cursor.execute("SELECT first_name, last_name FROM president WHERE death IS NULL").fetchall())

        # Fetch all wit name Suffix
        # pprint(cursor.execute("SELECT first_name, last_name FROM president WHERE suffix IS NOT NULL AND death IS NULL").fetchall())
        # Update president with last_name Trump and set suffix to NULL
        # cursor.execute('UPDATE president SET suffix = NULL WHERE last_name = "Trump"')
        # pprint(cursor.execute("SELECT first_name, last_name FROM president WHERE suffix IS NOT NULL AND death IS NULL").fetchall())
        #
        # # Fetch all presidents names ordered by last_name
        # # Decending and Ascending
        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY last_name DESC").fetchall())
        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY last_name ASC").fetchall())

        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY state DESC, last_name ASC").fetchall())
        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY state DESC, last_name DESC").fetchall())

        # Fetch all presidents that are the 5 first born
        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY birth ASC LIMIT 5").fetchall())

        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY birth ASC LIMIT 5").fetchall())
        # pprint(cursor.execute("SELECT first_name, last_name FROM president ORDER BY birth ASC LIMIT 5,5").fetchall())

        pprint(cursor.execute("""
            SELECT first_name, last_name, 
            CASE 
                WHEN death IS NULL THEN julianday('now') - julianday(birth)
                ELSE julianday(death) - julianday(birth)
            END as days_lived
            FROM president 
            ORDER BY days_lived DESC
            LIMIT 5
        """).fetchall())

        pprint(cursor.execute("SELECT first_name ||', '|| last_name as Name, state || ', ' || city as Place FROM president ORDER BY state").fetchall())