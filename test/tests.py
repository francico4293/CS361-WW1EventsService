import unittest

import requests


class TestWW1EventsApi(unittest.TestCase):
    __DAY = "day"
    __MONTH = "month"
    __URL = "http://localhost:5000/events"
    __JANUARY = 1
    __FEBRUARY = 2
    __DECEMBER = 12
    __DAYS_IN_JANUARY = 31
    __DAYS_IN_FEBRUARY = 28
    __DAYS_IN_DECEMBER = 31
    
    def test_api_response_january(self):
        for day in range(1, self.__DAYS_IN_JANUARY + 1):
            data = { self.__DAY: day, self.__MONTH: self.__JANUARY }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_february(self):
        for day in range(1, self.__DAYS_IN_FEBRUARY + 1):
            data = { self.__DAY: day, self.__MONTH: self.__FEBRUARY }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_december(self):
        for day in range(1, self.__DAYS_IN_DECEMBER + 1):
            data = { self.__DAY: day, self.__MONTH: self.__DECEMBER }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
