import csv
import sqlite3
from pprint import pprint
from contextlib import closing


def read_dict(file_path: str) -> list[dict[str, str]]:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        csv_tab = []
        for row in reader:
            csv_tab.append(row)
        return csv_tab  # NOQA


csv_table = read_dict("nasdaq_screener_1713244597669.csv")
# pprint(csv_table[:5])
data_nasdaq = [(row["Symbol"], row["Name"]) for row in csv_table]

csv_table = read_dict("AAPL_daily_close.csv")
# pprint(csv_table[:5])
data_aapl = [(row["date"], row["1. open"], row["2. high"], row["3. low"], row["4. close"], row["5. volume"]) for row in csv_table]

csv_table = read_dict("MSFT_daily_close.csv")
# pprint(csv_table[:5])
data_msft = [(row["date"], row["1. open"], row["2. high"], row["3. low"], row["4. close"], row["5. volume"]) for row in csv_table]

with closing(sqlite3.connect("stock.db3")) as connection:
    connection.row_factory = sqlite3.Row
    with closing(connection.cursor()) as cur:
        print("Version:", sqlite3.version, "\n")

        cur.execute("DROP TABLE IF EXISTS nasdaq")
        cur.execute("CREATE TABLE IF NOT EXISTS nasdaq(symbol TEXT PRIMARY KEY, name TEXT)")
        cur.executemany("INSERT INTO nasdaq(symbol, name) VALUES (?, ?)", data_nasdaq)
        fetch = cur.execute("SELECT * FROM nasdaq LIMIT 3").fetchall()
        print("NASDAQ")
        for row in fetch:
            pprint(dict(row))
        print("\n")
        connection.commit()

        cur.execute("DROP TABLE IF EXISTS aapl")
        cur.execute("CREATE TABLE IF NOT EXISTS aapl(date TEXT PRIMARY KEY, open REAL, high REAL, low REAL, close REAL, volume INTEGER)")
        cur.executemany("INSERT INTO aapl(date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?)", data_aapl)
        fetch = cur.execute("SELECT * FROM aapl LIMIT 3").fetchall()
        print("AAPL")
        for row in fetch:
            print(dict(row))
        print("\n")
        connection.commit()

        cur.execute("DROP TABLE IF EXISTS msft")
        cur.execute("CREATE TABLE IF NOT EXISTS msft(date TEXT PRIMARY KEY, open REAL, high REAL, low REAL, close REAL, volume INTEGER)")
        cur.executemany("INSERT INTO msft(date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?)", data_msft)
        fetch = cur.execute("SELECT * FROM msft LIMIT 3").fetchall()
        print("MSFT")
        for row in fetch:
            print(dict(row))
        print("\n")
        connection.commit()
