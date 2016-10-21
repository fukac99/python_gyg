LOCATIONS_URL = "https://api.getyourguide.com/1/locations"
LOCATION_URL = "https://api.getyourguide.com/1/locations/{}"
TOURS_URL = "https://api.getyourguide.com/1/tours"
TOUR_URL = "https://api.getyourguide.com/1/tours/{}"

#TODO picture format

import requests
import json
import datetime

class GetYourGuide(object):

    """
        This class implements the complete GetYourGuide 1.0 API. It offers access to the Locations API, Tours API.
        
        Arguments:
            api_key: Please request key here:
            cnt_language: the language in which the content is returned. Currently available languages: [u'de',
   u'en', u'es', u'zh', u'fr', u'it', u'ja', u'ko', u'pt', u'ru', u'he'] Default 'en'
            currency: currency, in which the content is returned. Default 'EUR'
   
    """

    def __init__(self, api_key, cnt_language="en", currency="EUR"):
        self._api_key = api_key
        self._base_params = {"cnt_language" : cnt_language, "currency": currency}

    @staticmethod
    def _get_clean_parameters(kwargs):
        """
            Clean the parameters by filtering out any parameters that have a None value.
        """
        return dict((k, v) for k, v in kwargs.items() if v is not None)

    def get_location(self, location_id):
        """
            This function implements the GetYourGuide location search. Supply a location id 
        """
        if location_id is None:
            raise GetYourGuide.RequiredParameterError("location_id must be set")
            
        kwargs = {}
        return self._query(LOCATION_URL.format(location_id), kwargs)
        
    def search_locations(self,
                         q=None,
                         coordinates=None,
                         location=None,
                         location_type=None):
        """
            This function implements the GetYourGuide location search. 
            
            Arguments:
                q: string, location in text (optional)
                coordinates: list, [lat, long, radius (in km, optional)]
                location: list, location ids as integers
                location_type: string, possible values CITY, POI, AREA 
        """
    
            
        kwargs = {"q": q,
                  "coordinates[]":coordinates,
                  "location[]":location,
                  "location_type":location_type}
        return self._query(LOCATIONS_URL, kwargs)
        
    def search_tours(self,
                     q=None,
                     coordinates=None,
                     location=None,
                     categories=None,
                     date=None,
                     sortfield="popularity",
                     sortdirection="DESC",
                     cond_language='en',
                     rating=None,
                     price=None,
                     duration=None,
                     flags=None):
        """
            This function implements the GetYourGuide tour search. Requires
            on of q, coordinates, categories or location to be specified
            
            Arguments:
                q: string, location in text 
                coordinates: list, [lat, long, radius (in km, optional)]
                location: list, location ids as integers
                categories: list, category ids as integers
                date: datetime object or list of datetime objects, 
                    check for tours that are offered on date
                    or between dates. If a single value is provided, 
                    the check will include tours available on that day.
                sortfield: string, sort results by 'popularity' (Default),
                        'duration', 'price', 'rating'
                sortdirection: string, direction of sort 'DESC' (Default), 'ASC'
                cond_language: string, language that the tour is conducted in (2-char ISO code), Default 'en'
                rating: integer, minimum rating for your tour (0-5)
                price: float or list of floats length 2, if float then maximum price, if list interpreted as [min, max]
                duration: integer or list of integer length 2, if int then maximum duration, if list interpreted as [min, max] (in minutes)
                flags: list of string, option:
                        private: Private Tour. The Lead Traveler (and his/her group) is the only participant.
                        wheelchair: Tour is accessible with a wheelchair.
                        skip-line: allows to skip the queue.
                        pick-up: Hotel pick-up possible.
                        special: Special offers only
                        free-sale-only: Only Tours that can be booked with immediate confirmation.
                        mobile-voucher: Only Tours for which the supplier accepts mobile vouchers
        """
        if (q is None) & (coordinates is None) & (location is None) & (categories is None):
            raise GetYourGuide.RequiredParameterError("Requires on of q, coordinates, categories or location to be specified")
        
        if date is not None:        
            if isinstance(date, datetime.datetime):
                date = [date]
            elif not isinstance(date, list):
                raise GetYourGuide.BadParameterError("Date should be either datetime object or list of two datetime objects")
            elif not isinstance(date[0], datetime.datetime):
                raise GetYourGuide.BadParameterError("Date should be either datetime object or list of two datetime objects")
            
        kwargs = {"q": q,
                  "coordinates[]":coordinates,
                  "location[]": location,
                  "categories[]": categories,
                  "date[]":date,
                  "cond_language":cond_language,
                  "rating":rating,
                  "price[]":price,
                  "duration[]": duration,
                  "flags[]": flags,
                  "sortfield": sortfield,
                  "sortdirection": sortdirection
                  }
        return self._query(LOCATIONS_URL, kwargs)
        
    def get_tour(self, tour_id=None):
        """
            This function implements the GetYourGuide location search. Supply a location id 
        """
        if tour_id is None:
            raise GetYourGuide.RequiredParameterError("tour_id must be set")
            
        kwargs = {}
        return self._query(TOUR_URL.format(tour_id), kwargs)


    def _query(self, url, kwargs):
        """
            All query methods have the same logic, so don't repeat it! Query the URL, parse the response as JSON, and check for errors. If all
            goes well, return the parsed JSON.
        """
        parameters = self._base_params
        parameters.update(GetYourGuide._get_clean_parameters(kwargs))
        print parameters
        head ={
                    "Accept": "application/json",
                    "X-ACCESS-TOKEN" : self._api_key
                  }
        response = requests.get(url, params=parameters, headers=head)
        response_json = json.loads(response.content) # it shouldn't happen, but this will raise a ValueError if the response isn't JSON

        #check for errors
        if 'errors' in response_json:
            error_message = ""
            for err in response_json['errors']:
                error_message += err["errorMessage"]
                error_message += " | "
            raise GetYourGuide.GetYourGuideError(error_message)

        # we got a good response, so return
        return response_json
        
class GetYourGuideError(Exception):

        """
            This class is used for all API errors.
        """
        pass
    
class RequiredParameterError(Exception):
    """
        this class is used for missing parameters errors        
    """
    pass

class BadParameterError(Exception):
    """
        this class is used for missing parameters errors        
    """
    pass