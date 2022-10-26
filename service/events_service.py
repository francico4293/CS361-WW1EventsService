from bs4 import BeautifulSoup

import re

import requests

from utils.date_parser import DateParser


class EventsService(object):
    __EVENT = "event"
    __EVENTS = "events"
    __YEAR = "year"
    __THEATER_FRONT_CAMPAIGN = "theater_front_campaign"
    __URL = "https://en.wikipedia.org/wiki/Timeline_of_World_War_I"
    __HTML_PARSER = "html.parser"
    __SPAN = "span"
    __ID = "id"
    __TABLE = "table"
    __TR = "tr"
    __TD = "td"
    __REPLACEMENT_EXPRESSION = "[ ][(]Details[)]|\[[1-9]{1,}\]"
    __WW1_YEARS = [1914, 1915, 1916]

    def __init__(self, date_parser: DateParser):
        self.__date_parser = date_parser
        self.__capture_events = False
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
        for year in self.__WW1_YEARS:
            # get WW1 events table by year
            events_table = soup.find(self.__SPAN, { self.__ID: str(year) }).find_next(self.__TABLE).find_all(self.__TR)
            
            # count number of events in WW1 event table
            num_rows = len(events_table)
            for row in range(1, num_rows):
                # get each row in WW1 events table
                row_data = events_table[row].find_all(self.__TD)
                row_data_length = len(row_data)

                # turn capture events flag on or off
                self.__capture_events = (self.__date_parser.is_date(row_data[0].text.strip()) and \
                    self.__date_parser.capture_events_for_date(row_data[0].text.strip(), year, month, day)) or \
                        (not self.__date_parser.is_date(row_data[0].text.strip()) and self.__capture_events)
                
                # stand alone date in row - no events can be capture from this row
                if row_data_length == 1: continue

                # if the data at index 0 in row_data array is a date and the client provided day and month is equal to or in the date range, then capture events
                if self.__capture_events:
                    # determine how long the event lasted and if there were multiple year occurences of the event for the day and month
                    event_year_offset_array = self.__date_parser.get_event_year_offset_array(row_data[0].text.strip(), year, month, day)

                    # if row_data at row_data_idx is a date then begin capture events at idx 1, otherwise start at idx 0
                    row_data_idx = 1 if self.__date_parser.is_date(row_data[0].text.strip()) else 0
                    # iterate over event data from row
                    while (row_data_idx < row_data_length):
                        # add event number of times given by event_duration
                        for year_offset in event_year_offset_array:
                            self.__events[self.__EVENTS].append({
                                self.__THEATER_FRONT_CAMPAIGN: row_data[row_data_idx].text.strip(),
                                self.__EVENT: re.sub(self.__REPLACEMENT_EXPRESSION, "", row_data[row_data_idx + 1].text.strip()),
                                self.__YEAR: year + year_offset
                            })
                        row_data_idx += 2
        
        return self.__events
