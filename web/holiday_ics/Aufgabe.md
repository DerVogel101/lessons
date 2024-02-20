# Holiday Scraper ICS Service

Entwickeln Sie eine einfache Web-Applikation mit dem Python 
[Bottle Framework](https://bottlepy.org) mit folgenden Eigenschaften:

- Unter der URL `/all` soll ein ICS Dokument mit allen 
  Ferien zurückgegeben werden.
- Unter den URLs der Form `/year/2024` sollen die 
  Ferientermine für das jeweilige Jahr als ICS Dokument 
  zurückgeliefert werden.

Verwenden Sie für die Erstellung der Kalenderdateien das
[`icalendar` Modul](). Verwenden Sie bei der Rückgabe den 
passenen Mime-Type. Überprüfen Sie die Ausgabe mit einem
Validator (z. B. <https://icalendar.org/validator.html>)

Für die Datenabfrage kann das Modul `holiday_scraper`
verwendet werden (siehe `demo`).

## Zusatzaufgabe

Entwickeln Sie ein Modul `glocke_scraper`, dass den aktuellen
Spielplan des Konzerthauses *Die Glocke* von der Website <https://www.glocke.de/tickets-programm/> 
ausließt und integrieren Sie dieses in ihr Programm unter der 
URL `/glocke`. 

Versuchen Sie dabei, so viel Code wie möglich 
aus ihrer bestehenden Applikation erneut zu verwenden, ohne ihn
zu kopieren. Passen Sie das bisherige Programm dazu
entsprechend an.