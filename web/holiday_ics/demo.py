from pprint import pprint
import holiday_scraper
import icalendar
from datetime import datetime
import random


def add_event(calendar: icalendar.Calendar, date_start: datetime, date_end: datetime, name: str) -> None:
    event = icalendar.Event()
    event.add('summary', name)
    event.add('dtstart', date_start)
    event.add('dtend', date_end)
    event.add('dtstamp', datetime.now())
    event.add('uid', random.SystemRandom().getrandbits(128))
    calendar.add_component(event)


def select_year(holidays: dict, selection: str) -> dict:
    year: list[str] = list(holidays.keys())
    if selection == "all":
        return holidays
    else:
        for key in year:
            if key[:4] == selection:
                selection = key
                break
        else:
            raise Exception("Year not found: " + selection)
        print("The selected year:", selection)
        return {selection: holidays[selection]}


def rectify_dumb_dates(date: str, year: str) -> tuple:
    year = int(year[-4:])
    month_dict = {"Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6, "Juli": 7, "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12}
    date = date.split() if " " in date else date.split(".")
    day = int(date[0].strip("."))
    month = month_dict[date[1]] if date[1] in month_dict else int(date[1])
    return day, month, year





if __name__ == "__main__":
    holidays = holiday_scraper.get_holidays()
    pprint(holidays)

    selcted_year_key = str(2023)
    selected_year = select_year(holidays, selcted_year_key)
    pprint(selected_year)

    for year in selected_year:
        for holiday in selected_year[year]:
            print(year, holiday)
            dates = []
            # TODO: finish this
            for date in selected_year[year][holiday]:
                date = rectify_dumb_dates(date, holiday)
                dates.append(date)
                print(date)

    cal = icalendar.Calendar()
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')

    add_event(cal, datetime(2024, 1, 1), datetime(2024, 1, 1), "New Year's Day")

    # Save the calendar to a file
    with open('test_event.ics', 'wb') as f:
        f.write(cal.to_ical())

        print("Event saved to test_event.ics")
