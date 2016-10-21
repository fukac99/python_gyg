from unittest import TestCase

import python_gyg

GYG_API_KEY = "CgV4oG41Z7ZtfYJqlyPfYByvInsPRXJvlzUm6DgBoKYDJpy7"

class TestLocation(TestCase):
    def test_is_GetYourGuide_isntance(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue(isinstance(s, python_gyg.GetYourGuide))
        
    def get_location_param_error(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertRaises(python_gyg.GetYourGuide.RequiredParameterError, s.get_location())
        
    def get_location_gyg_error(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertRaises(python_gyg.GetYourGuide.RequiredParameterError, s.get_location(10000000))
    
    def get_location_newyork(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue((s.get_location(59))["data"]["locations"][0]["name"] == "New York")

class TestTour(TestCase):        
    def get_tour_param_error(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertRaises(python_gyg.GetYourGuide.RequiredParameterError, s.get_tour())
        
    def get_tour_gyg_error(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertRaises(python_gyg.GetYourGuide.RequiredParameterError, s.get_tour(10000000))
    
    def get_tour_newyork(self):
        s = python_gyg.GetYourGuide(GYG_API_KEY)
        self.assertTrue((s.get_tour(20434))["data"]["tours"][0]["title"] == "New York Photography Experience by Night")