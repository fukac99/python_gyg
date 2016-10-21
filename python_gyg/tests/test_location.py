from unittest import TestCase

import python_gyg
import datetime

GYG_API_KEY = "<your_api_key>"

class TestLocation(TestCase):
    def test_is_GetYourGuide_isntance(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s, python_gyg.GetYourGuide))
        
#    def test_get_location_param_error(self):
#        s = python_gyg.GetYourGuide(GYG_API_KEY)
#        self.assertRaises(python_gyg.RequiredParameterError, s.get_location())
#        
#    def test_get_location_gyg_error(self):
#        s = python_gyg.GetYourGuide(GYG_API_KEY)
#        self.assertRaises(python_gyg.GetYourGuideError, s.get_location(10000000))
    
    def test_get_location_newyork(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue((s.get_location(59))["data"]["locations"][0]["name"] == "New York")

class TestTour(TestCase):        
#    def test_get_tour_param_error(self):
#        s = python_gyg.GetYourGuide(GYG_API_KEY)
#        self.assertRaises(python_gyg.RequiredParameterError, s.get_tour())
#        
#    def test_get_tour_gyg_error(self):
#        s = python_gyg.GetYourGuide(GYG_API_KEY)
#        self.assertRaises(python_gyg.GetYourGuideError, s.get_tour(10000000))
    
    def test_get_tour_newyork(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue((s.get_tour(20434))["data"]["tours"][0]["title"] == "New York Photography Experience by Night")
        
class TestSearchTours(TestCase):        
#    def test_search_tour_param_error(self):
#        s = python_gyg.GetYourGuide(GYG_API_KEY)
#        self.assertRaises(python_gyg.RequiredParameterError, s.search_tours())
#        
#    def test_search_tour_bad_param_error(self):
#        s = python_gyg.GetYourGuide(GYG_API_KEY)
#        self.assertRaises(python_gyg.BadParameterError, s.search_tours(q="New York", date=332))
#        
#    def test_search_tour_bad_param_error2(self):
#        s = python_gyg.GetYourGuide(GYG_API_KEY)
#        self.assertRaises(python_gyg.BadParameterError, s.search_tours(q="New York", date=[42, 42]))
#    
    def test_search_tour_one_date(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(q="New York", date=datetime.datetime.now()), dict))
        
    def test_search_tour_two_dates(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(q="New York",
                                                  date=[datetime.datetime.now(), 
                                                        datetime.datetime.now()]),
 dict))
 
    def test_search_tour_by_coordinates(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(coordinates=[40.75, -73.97, 10]), dict))
        
    def test_search_tour_by_categories(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(categories=[1,2]), dict))
        
    def test_search_tour_by_location(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(location=[59, 109]), dict))
        
    def test_search_tour_by_one_price(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(coordinates=[40.75, -73.97, 10], price=30), dict))
    
    def test_search_tour_by_price_range(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(coordinates=[40.75, -73.97, 10], price=[30, 60]), dict))
    
    def test_search_tour_by_max_duration(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(coordinates=[40.75, -73.97, 10], duration=120), dict))
        
    def test_search_tour_by_duration_range(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_tours(coordinates=[40.75, -73.97, 10], duration=[30, 260]), dict))
        
class TestSearchLocations(TestCase):
    def test_search_locations_by_coordinates(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_locations(coordinates=[40.75, -73.97, 10]), dict))
    
    def test_search_locations_by_query(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_locations(q="New York"), dict))
        
    def test_search_locations_by_location(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s.search_locations(location=59), dict))
    