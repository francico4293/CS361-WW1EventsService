import re

from datetime import date


class DateParser(object):
    __DATE_EXPRESSION_1 = "^[A-Za-z]{3,}[ ][0-9]{1,}$"
    __DATE_EXPRESSION_2 = "^[A-Za-z]{3,}[ ][0-9]{1,}[–][0-9]{1,}$"
    __DATE_EXPRESSION_3 = "^[A-Za-z]{3,}[ ][0-9]{1,}[ ][–][ ][A-Za-z]{3,}[ ][0-9]{1,}$"
    __DATE_EXPRESSION_4 = "^[A-Za-z]{3,}[ ][0-9]{1,}[ ][–][ ][A-Za-z]{3,}[ ][0-9]{1,}[,][ ][1-9]{4}$"
    __SPACE_CHAR = ' '
    __EN_DASH = '–'
    __DATE_STR_TO_NUM_MAP = {
        "JAN": 1, "FEB": 2, "MAR": 3, 
        "APR": 4, "MAY": 5, "JUN": 6,
        "JUL": 7, "AUG": 8, "SEP": 9, 
        "OCT": 10, "NOV": 11, "DEC": 12
    }
    __DAYS_IN_MONTH_MAP = {
        "JAN": 31, "FEB": 28, "MAR": 31, 
        "APR": 30, "MAY": 31, "JUN": 30,
        "JUL": 31, "AUG": 31, "SEP": 30, 
        "OCT": 31, "NOV": 30, "DEC": 31
    }

    def is_date(self, string: str) -> bool:
        return (
            re.search(self.__DATE_EXPRESSION_1, string) or re.search(self.__DATE_EXPRESSION_2, string) or \
            re.search(self.__DATE_EXPRESSION_3, string) or re.search(self.__DATE_EXPRESSION_4, string)
        )
    
    def capture_events_for_date(self, date_string_to_parse: str, ww1_year: int, month: int, day: int) -> bool:
        if (re.search(self.__DATE_EXPRESSION_1, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_1(date_string_to_parse, ww1_year)
            return parsed_date_string == date(ww1_year, month, day)
        elif (re.search(self.__DATE_EXPRESSION_2, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_2(date_string_to_parse, ww1_year)
            return parsed_date_string[0] <= date(ww1_year, month, day) <= parsed_date_string[1]

        return False
    
    def __date_expression_parser_1(self, date_string_to_parse: str, ww1_year: int) -> date:
        try:
            parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
            return date(
                ww1_year, 
                self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                int(parsed_date[1])
            )
        except ValueError:
            return date(
                ww1_year, 
                self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                self.__DAYS_IN_MONTH_MAP[parsed_date[0][:3].upper()]
            )

    def __date_expression_parser_2(self, date_string_to_parse: str, ww1_year: int) -> list:
        try:
            parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
            parsed_days = parsed_date[1].split(self.__EN_DASH)
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    int(parsed_days[0])
                ),
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    int(parsed_days[1])
                )
            ]
        except ValueError:
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    int(parsed_days[0])
                ),
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    self.__DAYS_IN_MONTH_MAP[parsed_date[0][:3].upper()]
                )
            ]
