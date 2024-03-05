SQLite3 Cheat Sheet

- Datatypes:  
  Each value stored in an SQLite database (or manipulated by the database engine) has one of the following storage classes:
   - NULL. The value is a NULL value.
   - INTEGER. The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
   - REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
   - TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
   - BLOB. The value is a blob of data, stored exactly as it was input.

1. Database Connection:
   - Open a database connection: `sqlite3 <database_name>.db`
   - Connect to an existing database: `.open <database_name>.db`
   - Exit the SQLite3 prompt: `.exit`

2. Database Operations:
   - Create a new database: `sqlite3 <database_name>.db`
   - Attach another database: `ATTACH DATABASE '<database_name>.db' AS <alias>`
   - Detach a database: `DETACH DATABASE <alias>`

3. Table Operations:
   - Create a new table: `CREATE TABLE <table_name> (<column1> <datatype1>, <column2> <datatype2>, ...)`
   - Show all tables in the database: `.tables`
   - Describe a table: `.schema <table_name>`
   - Rename a table: `ALTER TABLE <old_table_name> RENAME TO <new_table_name>`
   - Delete a table: `DROP TABLE <table_name>`

4. Data Manipulation:
   - Insert a new row: `INSERT INTO <table_name> (<column1>, <column2>, ...) VALUES (<value1>, <value2>, ...)`
   - Update existing rows: `UPDATE <table_name> SET <column1> = <new_value1>, <column2> = <new_value2> WHERE <condition>`
   - Delete rows: `DELETE FROM <table_name> WHERE <condition>`
   - Select rows: `SELECT <column1>, <column2>, ... FROM <table_name> WHERE <condition>`

5. Querying:
   - Filter rows: `WHERE <condition>`
   - Sort rows: `ORDER BY <column> [ASC|DESC]`
   - Limit number of rows: `LIMIT <number>`
   - Join tables: `SELECT <columns> FROM <table1> JOIN <table2> ON <condition>`
   - Group rows: `SELECT <columns> FROM <table_name> GROUP BY <column>`

6. Functions:
   - Aggregation functions: `COUNT(), SUM(), AVG(), MIN(), MAX()`
   - String functions: `LENGTH(), UPPER(), LOWER(), SUBSTR(), REPLACE()`
   - Date and time functions: `DATE(), TIME(), DATETIME(), STRFTIME()`

7. Indexing:
   - Create an index: `CREATE INDEX <index_name> ON <table_name> (<column>)`
   - Drop an index: `DROP INDEX <index_name>`

8. Transactions:
   - Begin a transaction: `BEGIN TRANSACTION`
   - Commit a transaction: `COMMIT`
   - Rollback a transaction: `ROLLBACK`

Note: Replace `<database_name>`, `<table_name>`, `<column>`, `<value>`, `<condition>`, `<index_name>`, and `<alias>` with the appropriate names or values in your specific case.