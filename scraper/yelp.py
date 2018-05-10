import requests


class Yelp:

    def __init__(self, api_key):

        # retrieves the api key from storage
        self.api_key = api_key

        # creates a variable for the api host
        self.api_host = 'https://api.yelp.com/v3/businesses/search'

    def request(self, params=None):
        """
        Creates a get request to the api host with the specified parameters.

        :param params: the parameters that will be used in the get request
        :return response: the response from the api host
        """

        # if params is none, set it to an empty dictionary
        params = params or {}

        # creates the header containing the api key
        headers = {
            'Authorization': 'Bearer %s' % self.api_key,
        }

        # make the get request to the api host and store the response
        response = requests.request('GET', self.api_host, headers=headers, params=params)

        # return the processed json response
        return response.json()

    def search(self, name, location):
        """
        Given the business name and location, return the business information.

        :param name: the name of the business
        :param location: the location of the business
        :return request: the keys about the business of interest
        """

        # packages the params into a dictionary
        params = {
            'term': name.replace(' ', '+'),
            'location': location.replace(' ', '+'),
            'limit': 1
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
            return [result['businesses'][0]['name'], result['businesses'][0]['categories'][0]['title']]

        # if there is no data at a specific key
        except KeyError:

            # return a 'None' array
            return ['None', 'None']

        # if there is no data at a specified index
        except IndexError:

            # return a 'None' array
            return ['None', 'None']

    def test(self):
        return self.get_category("Chipotle Mexican Grill", "32217")[0] == "Chipotle Mexican Grill"