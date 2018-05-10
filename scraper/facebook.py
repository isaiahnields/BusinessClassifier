import requests
from geopy import geocoders
from geopy.exc import GeocoderTimedOut


class Facebook:

    def __init__(self):
        """
        Initializes the member variables for the facebook api.
        """

        # retrieves the api key from storage
        self.access_token = open("../data/facebook.txt", 'r').read()

        # creates a variable for the api host
        self.api_host = 'https://graph.facebook.com/v3.0/search'

        # sets up geocoder to convert city and state into coordinates
        self.user_name = open("../data/geonames.txt", 'r').read()
        self.geocoder = geocoders.GeoNames(username=self.user_name)

    def request(self, params=None):
        """
        Creates a get request to the api host with the specified parameters.

        :param params: the parameters that will be used in the get request
        :return response: the response from the api host
        """

        # if params is none, set it to an empty dictionary
        params = params or {}

        # make the get request to the api host and store the response
        response = requests.request('GET', self.api_host, params=params)

        # return the processed json response
        return response.json()

    def search(self, name, location):
        """
        Given the business name and location, return the business information.

        :param name: the name of the business
        :param location: the location of the business
        :return request: the keys about the business of interest
        """

        # uses geocoder to get the coordinates the from city and state information
        coordinates = self.geocoder.geocode(location)[1]
        center = str(coordinates[0]) + ',' + str(coordinates[1])

        # packages the params into a dictionary
        params = {
            'type': 'place',
            'q': name,
            'center': center,
            'fields': 'name,category_list',
            'access_token': self.access_token
        }

        # makes and returns the request
        return self.request(params)

    def get_category(self, name, location):
        """
        Given the business name and location, return the business name and category.

        :param name: the name of the business that should be searched
        :param location: the location of the business that should be searched
        :return result: an array containing the business name and category
        """

        try:

            # search for the business by its name and location
            result = self.search(name, location)

            # return an array containing the business name and category
            return [result['data'][0]['name'], result['data'][0]['category_list'][0]['name']]

        # if there is no data at a specific key
        except KeyError:

            # return a 'None' array
            return ['None', 'None']

        # if there is no data at a specified index
        except IndexError:

            # return a 'None' array
            return ['None', 'None']

        # if the the geocoder could not process the request
        except GeocoderTimedOut:

            # return a 'Timeout' array
            return ['Timeout', 'Timeout']
