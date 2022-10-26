import unittest

import requests


class TestWW1EventsApi(unittest.TestCase):
    __DAY = "day"
    __MONTH = "month"
    __URL = "http://localhost:5000/events"
    __JANUARY = 1
    __FEBRUARY = 2
    __MARCH = 3
    __APRIL = 4
    __MAY = 5
    __JUNE = 6
    __JULY = 7
    __AUGUST = 8
    __SEPTEMBER = 9
    __DECEMBER = 12
    __DAYS_IN_JANUARY = 31
    __DAYS_IN_FEBRUARY = 28
    __DAYS_IN_MARCH = 31
    __DAYS_IN_APRIL = 30
    __DAYS_IN_MAY = 31
    __DAYS_IN_JUNE = 30
    __DAYS_IN_JULY = 31
    __DAYS_IN_AUGUST = 31
    __DAYS_IN_SEPTEMBER = 30 
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
    
    def test_api_response_march(self):
        for day in range(1, self.__DAYS_IN_MARCH + 1):
            data = { self.__DAY: day, self.__MONTH: self.__MARCH }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_april(self):
        for day in range(1, self.__DAYS_IN_APRIL + 1):
            data = { self.__DAY: day, self.__MONTH: self.__APRIL }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_may(self):
        for day in range(1, self.__DAYS_IN_MAY + 1):
            data = { self.__DAY: day, self.__MONTH: self.__MAY }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_june(self):
        for day in range(1, self.__DAYS_IN_JUNE + 1):
            data = { self.__DAY: day, self.__MONTH: self.__JUNE }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_july(self):
        for day in range(1, self.__DAYS_IN_JULY + 1):
            data = { self.__DAY: day, self.__MONTH: self.__JULY }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_august(self):
        for day in range(1, self.__DAYS_IN_AUGUST + 1):
            data = { self.__DAY: day, self.__MONTH: self.__AUGUST }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_september(self):
        for day in range(1, self.__DAYS_IN_SEPTEMBER + 1):
            data = { self.__DAY: day, self.__MONTH: self.__SEPTEMBER }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)
    
    def test_api_response_december(self):
        for day in range(1, self.__DAYS_IN_DECEMBER + 1):
            data = { self.__DAY: day, self.__MONTH: self.__DECEMBER }
            response = requests.get(self.__URL, json=data)
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
