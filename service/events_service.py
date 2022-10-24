from bs4 import BeautifulSoup

import requests

from utils.date_parser import DateParser


class EventsService(object):
    __EVENTS = "events"
    __URL = "https://en.wikipedia.org/wiki/Timeline_of_World_War_I"
    __HTML_PARSER = "html.parser"
    __SPAN = "span"
    __ID = "id"
    __TABLE = "table"
    __TD = "td"
    __YEARS = [1914]

    def __init__(self, date_parser: DateParser):
        self.__date_parser = date_parser
        self.__events = { self.__EVENTS: [] }

    def get_events(self, day: str, month: str) -> dict:
        # cast day and month to integer values
        day = int(day)
        month = int(month)

        # get WW1 events page for web scraping
        events_page = requests.get(self.__URL)
        # parse WW1 events page
        soup = BeautifulSoup(events_page.content, self.__HTML_PARSER)

        # iterate over each WW1 year
        for year in self.__YEARS:
            events_table = soup.find(self.__SPAN, { self.__ID: str(year) }).find_next(self.__TABLE).find_all(self.__TD)
            
            row, num_rows = 0, len(events_table)
            while (row < num_rows):
                if self.__date_parser.is_date(events_table[row].text.strip()):
                    print(events_table[row].text.strip())
                    
                row += 1
