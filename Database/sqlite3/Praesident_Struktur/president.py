import sqlite3
from contextlib import closing
from pprint import pprint
import json
from datetime import datetime

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

        # Fetch all presidents that are the 5 oldest and are alive
        # pprint(cursor.execute("""
        #     SELECT first_name, last_name,
        #     CASE
        #         WHEN death IS NULL THEN julianday('now') - julianday(birth)
        #         ELSE julianday(death) - julianday(birth)
        #     END as days_lived
        #     FROM president
        #     ORDER BY days_lived DESC
        #     LIMIT 5
        # """).fetchall())

        # Select all presidents first_name and last_name and state and city, that are living, sorted by name and combined with ', '
        # pprint(cursor.execute("SELECT first_name ||', '|| last_name as Name, city || ', ' || state as Place FROM president WHERE death IS NULL ORDER BY Name").fetchall())

        # Select all presidents containing the letter V in the state at the beginning
        # pprint(cursor.execute("SELECT * FROM president WHERE state like 'V%'").fetchall())

        # Select all presidents containing the letter V in the state at the end
        # pprint(cursor.execute("SELECT * FROM president WHERE state like '%V'").fetchall())

        # Select all Presidents that are alive and have a suffix
        # pprint(cursor.execute("SELECT * FROM president WHERE death IS NULL AND suffix IS NOT NULL").fetchall())

        # Select all Presidents that died between 1970(inclusive) and 1980(inclusive)
        # pprint(cursor.execute("SELECT * FROM president WHERE death >= '1970%' and death <= '1980%'").fetchall())
        # pprint(cursor.execute("SELECT * FROM president WHERE death between '1970-01-01' and '1980-12-31'").fetchall())

        # Select all Presidents that are born in march
        # pprint(cursor.execute("SELECT first_name ||', '|| last_name as Name, birth FROM president WHERE birth like '%-03-%'").fetchall())

        # 17. Show all presidents including their age as age sorted by age in days
        # pprint(cursor.execute("""
        #     SELECT first_name ||', '|| last_name as Name,
        #     CASE
        #         WHEN death IS NULL THEN julianday('now') - julianday(birth)
        #         ELSE julianday(death) - julianday(birth)
        #     END as age
        #     FROM president
        #     ORDER BY age DESC
        # """).fetchall())

        # 18. Show all presidents who have/would have a birthday within the current montn, Pattern comparison with _ and %
        # pprint(cursor.execute("""
        #     SELECT first_name ||', '|| last_name as Name, birth
        #     FROM president
        #     WHERE birth like '%-' || ? || '-%'
        #     """, (f"{datetime.now().month:0>2}",)).fetchall())

        # 19. Show all presidents whose last name begins with W
        # pprint(cursor.execute("""
        #     SELECT first_name ||', '|| last_name as Name
        #     FROM president
        #     WHERE last_name like 'W%'
        #     """).fetchall())

        # 20. Show all presidents whose last name contains a W
        # pprint(cursor.execute("""
        #     SELECT first_name ||', '|| last_name as Name
        #     FROM president
        #     WHERE last_name like '%W%'
        #     """).fetchall())

        # 21. Show all presidents whose names are 4 letters long
        # pprint(cursor.execute("""
        #     SELECT first_name ||', '|| last_name as Name
        #     FROM president
        #     WHERE length(last_name) = 4
        #     """).fetchall())

        # 22. Show all states from which a president came/comes (with and without repetition)### Count with count()
        # pprint(cursor.execute("""
        #     SELECT state, COUNT(state) as count
        #     FROM president
        #     GROUP BY state
        #     """).fetchall())

        # 23. Show the number of presidents in the table
        # pprint(cursor.execute("""
        #     SELECT COUNT(*) as count
        #     FROM president
        #     """).fetchall())

        # 24. Show the number of dead presidents
        # pprint(cursor.execute("""
        #     SELECT COUNT(*) as count
        #     FROM president
        #     WHERE death IS NOT NULL
        #     """).fetchall())

        # 24. How many states did the presidents come from?
        # pprint(cursor.execute("""
        #     SELECT COUNT(DISTINCT state) as count
        #     FROM president
        #     """).fetchall())

        # 25. Show the number of presidents per state sorted by frequency
        # pprint(cursor.execute("""
        #     SELECT state, COUNT(state) as count
        #     FROM president
        #     GROUP BY state
        #     ORDER BY count DESC
        #     """).fetchall())

        # 26. Show a list of months and the number of presidents born in them
        # pprint(cursor.execute("""
        #     SELECT substr(birth, 6, 2) as month, COUNT(substr(birth, 6, 2)) as count
        #     FROM president
        #     GROUP BY month
        #     ORDER BY month ASC
        #     """).fetchall())

        # 27. Show the number of presidents per state sorted by frequency for states with more than one president
        # pprint(cursor.execute("""
        #     SELECT state, COUNT(state) as count
        #     FROM president
        #     GROUP BY state
        #     HAVING count > 1
        #     ORDER BY count DESC
        #     """).fetchall())

        # 28. Which state has produced the most presidents?
        # pprint(cursor.execute("""
        #             SELECT state, COUNT(state) as count
        #             FROM president
        #             GROUP BY state
        #             ORDER BY count DESC LIMIT 1
        #             """).fetchall())

        cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
        cursor.execute("INSERT INTO user (name, email) VALUES ('John Doe', 'john@doe.com')")
        cursor.execute("INSERT INTO user (name, email) VALUES ('Jane Doe', 'jane@doe.com')")

        pprint(cursor.execute("SELECT * FROM user").fetchall())
