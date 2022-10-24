from bs4 import BeautifulSoup

import requests


class EventsService(object):
    EVENTS = "events"
    URL = "https://en.wikipedia.org/wiki/Timeline_of_World_War_I"
    HTML_PARSER = "html.parser"
    YEARS = [1914]

    def __init__(self):
        self.__events = { self.EVENTS: [] }

    def get_events(self, day: str, month: str) -> dict:
        if (type(day) != int):
            day = int(day)

        if (type(month) != int):
            month = int(month)

        print(type(day), type(month))

        events_page = requests.get(self.URL)
        soup = BeautifulSoup(events_page.content, self.HTML_PARSER)

        for year in self.YEARS:
            pass
