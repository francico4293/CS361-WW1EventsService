import re

from datetime import date


class DateParser(object):
    __DATE_EXPRESSION_1 = "^[A-Za-z]{3,}[ ][0-9]{1,}$"
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
        return re.search(self.__DATE_EXPRESSION_1, string)
