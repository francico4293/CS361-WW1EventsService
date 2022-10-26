import re

from datetime import date


class DateParser(object):
    __DATE_EXPRESSION_1 = "^[A-Za-z]{3,}[ ][0-9]{1,}$"
    __DATE_EXPRESSION_2 = "^[A-Za-z]{3,}[ ][0-9]{1,}[–][0-9]{1,}$"
    __DATE_EXPRESSION_3 = "^[A-Za-z]{3,}[ ][0-9]{1,}[ ][–][ ][A-Za-z]{3,}[ ][0-9]{1,}$"
    __DATE_EXPRESSION_4 = "^[A-Za-z]{3,}[ ][0-9]{1,}[ ][–][ ][A-Za-z]{3,}[ ][0-9]{1,}[,][ ][1-9]{4}$"
    __DATE_EXPRESSION_5 = "^[A-Za-z]{3,}[0-9]{1,}[–][0-9]{1,}$"
    __DATE_EXPRESSION_6 = "^[A-Za-z]{3,}[–][A-Za-z]{3,}[ ][0-9]{1,}[,][ ][1-9]{4}$"
    __DATE_EXPRESSION_7 = "^[A-Za-z]{3,}[ ][0-9]{1,}[ ][–][ ][0-9]{1,}[ ][A-Za-z]{3,}[ ][1-9]{4}$"
    __SPACE_CHAR = ' '
    __EN_DASH = '–'
    __COMMA_CHAR = ','
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
            re.search(self.__DATE_EXPRESSION_3, string) or re.search(self.__DATE_EXPRESSION_4, string) or \
            re.search(self.__DATE_EXPRESSION_5, string) or re.search(self.__DATE_EXPRESSION_6, string) or \
            re.search(self.__DATE_EXPRESSION_7, string)
        )
    
    def capture_events_for_date(self, date_string_to_parse: str, ww1_year: int, month: int, day: int) -> bool:
        if (re.search(self.__DATE_EXPRESSION_1, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_1(date_string_to_parse, ww1_year)
            return parsed_date_string == date(ww1_year, month, day)
        elif (re.search(self.__DATE_EXPRESSION_2, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_2(date_string_to_parse, ww1_year)
            return parsed_date_string[0] <= date(ww1_year, month, day) <= parsed_date_string[1]
        elif (re.search(self.__DATE_EXPRESSION_3, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_3(date_string_to_parse, ww1_year)
            return parsed_date_string[0] <= date(ww1_year, month, day) <= parsed_date_string[1]
        elif (re.search(self.__DATE_EXPRESSION_4, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_4(date_string_to_parse, ww1_year)
            return parsed_date_string[0] <= date(ww1_year, month, day) <= parsed_date_string[1]
        elif (re.search(self.__DATE_EXPRESSION_5, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_5(date_string_to_parse, ww1_year)
            return parsed_date_string[0] <= date(ww1_year, month, day) <= parsed_date_string[1]
        elif (re.search(self.__DATE_EXPRESSION_6, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_6(date_string_to_parse, ww1_year)
            return parsed_date_string[0] <= date(ww1_year, month, day) <= parsed_date_string[1]
        elif (re.search(self.__DATE_EXPRESSION_7, date_string_to_parse)):
            parsed_date_string = self.__date_expression_parser_7(date_string_to_parse, ww1_year)
            return parsed_date_string[0] <= date(ww1_year, month, day) <= parsed_date_string[1]

        return False
    
    def get_event_duration_in_years(self, date_string_to_parse: str, ww1_year: int, month: int, day: int) -> int:
        event_duration = 0;

        if re.search(self.__DATE_EXPRESSION_4, date_string_to_parse):
            start_date, end_date = self.__date_expression_parser_4(date_string_to_parse, ww1_year)
            end_date = date(end_date.year, month, day) if date(end_date.year, month, day) < end_date else date(end_date.year - 1, month, day)
            return (end_date.year - start_date.year) + 1
        
        return event_duration + 1
        
    
    def __date_expression_parser_1(self, date_string_to_parse: str, ww1_year: int) -> date:
        parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
        try:
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
        parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
        parsed_days = parsed_date[1].split(self.__EN_DASH)
        try:
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
    
    def __date_expression_parser_3(self, date_string_to_parse: str, ww1_year: int) -> list:
        parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
        try:
            return [
                date(
                    ww1_year,
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()],
                    int(parsed_date[1])
                ),
                date(
                    ww1_year,
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[3][:3].upper()],
                    int(parsed_date[4])
                )
            ]
        except ValueError:
            return [
                date(
                    ww1_year,
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()],
                    self.__DAYS_IN_MONTH_MAP[parsed_date[0][:3].upper()]
                ),
                date(
                    ww1_year,
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[3][:3].upper()],
                    self.__DAYS_IN_MONTH_MAP[parsed_date[3][:3].upper()]
                )
            ]

    def __date_expression_parser_4(self, date_string_to_parse: str, ww1_year: int) -> list:
        parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
        try:
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    int(parsed_date[1])
                ),
                date(
                    ww1_year + (int(parsed_date[5]) - ww1_year), 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[3][:3].upper()], 
                    int(parsed_date[4].split(self.__COMMA_CHAR)[0])
                )
            ]
        except ValueError:
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    self.__DAYS_IN_MONTH_MAP[parsed_date[0][:3].upper()]
                ),
                date(
                    ww1_year + (int(parsed_date[5]) - ww1_year), 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[3][:3].upper()], 
                    self.__DAYS_IN_MONTH_MAP[parsed_date[3][:3].upper()]
                )
            ]
    
    def __date_expression_parser_5(self, date_string_to_parse: str, ww1_year: int) -> list:
        try:
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[date_string_to_parse[:3].upper()], 
                    int(date_string_to_parse[3:4])
                ),
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[date_string_to_parse[:3].upper()], 
                    int(date_string_to_parse[5:])
                )
            ]
        except ValueError:
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[date_string_to_parse[:3].upper()], 
                    int(date_string_to_parse[3:4])
                ),
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[date_string_to_parse[:3].upper()], 
                    self.__DAYS_IN_MONTH_MAP[date_string_to_parse[:3].upper()]
                )
            ]
    
    def __date_expression_parser_6(self, date_string_to_parse: str, ww1_year: int) -> list:
        parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
        try:
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    1
                ),
                date(
                    ww1_year + (int(parsed_date[2]) - ww1_year), 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][4:].upper()], 
                    int(parsed_date[1].split(',')[0].upper())
                )
            ]
        except ValueError:
            return [
                date(
                    ww1_year, 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()], 
                    1
                ),
                date(
                    ww1_year + (int(parsed_date[2]) - ww1_year), 
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][4:].upper()], 
                    self.__DAYS_IN_MONTH_MAP[parsed_date[0][4:].upper()]
                )
            ]

    def __date_expression_parser_7(self, date_string_to_parse: str, ww1_year: int) -> list:
        parsed_date = date_string_to_parse.split(self.__SPACE_CHAR)
        try:
            return [
                date(
                    ww1_year,
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()],
                    int(parsed_date[1])
                ),
                date(
                    ww1_year + (int(parsed_date[5]) - ww1_year),
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[4][:3].upper()],
                    int(parsed_date[3])
                )
            ]
        except ValueError:
            return [
                date(
                    ww1_year,
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[0][:3].upper()],
                    self.__DAYS_IN_MONTH_MAP[parsed_date[0][:3].upper()]
                ),
                date(
                    ww1_year + (int(parsed_date[5]) - ww1_year),
                    self.__DATE_STR_TO_NUM_MAP[parsed_date[4][:3].upper()],
                    self.__DAYS_IN_MONTH_MAP[parsed_date[4][:3].upper()]
                )
            ]
