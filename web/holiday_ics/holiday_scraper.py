# Scraper to get holydays from the internet
from pprint import pprint

import requests
from bs4 import BeautifulSoup as Soup

# Positionen in den Tabellen
TD_H_END = 4
TD_H_START = 2
TD_H_NAME = 0

# Download url and parse with beautiful soup
url = "https://www.transparenz.bremen.de/metainformationen/verordnung-ueber-die-ferien-fuer-die-schulen-der-stadtgemeinden-bremen-und-bremerhaven-fuer-die-schuljahre-2017-2018-bis-2023-2024-vom-1-november-2015-154102?asl=bremen203_tpgesetz.c.55340.de&template=20_gp_ifg_meta_detail_d"


def get_holidays():
    page = requests.get(url)
    soup = Soup(page.content, "html.parser")

    doc_contents = soup.find_all("div", class_="docLayoutText")
    assert 2 == len(doc_contents)  # shoud find two
    doc_content = doc_contents[0]  # use first one
    tables = doc_content.find_all("table")

    holidays = {} # Schuljahr -> (Ferienname -> ( Start, Ende ))
    for table in tables:
        first_td = table.find("td")
        if first_td.text.strip().startswith("Ferientermine"):
            year = first_td.text.strip().split()[-1]  # Schuljahr
            holidays[year] = {}  # prepare
            for row in table.find_all("tr")[2:]:  # ignore first entry and heading
                tds = row.find_all("td")
                name, start, end = tds[TD_H_NAME].text, tds[TD_H_START].text, tds[TD_H_END].text
                name, start, end = map(lambda x:x.strip(), (name, start, end))
                if all(map(lambda x:len(x) > 0, (name, start, end))):
                    holidays[year][name] = (start, end)

    return holidays