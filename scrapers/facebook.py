import os
import requests
from urllib.parse import quote
from geopy import geocoders
from geopy.exc import GeocoderTimedOut

# get the root directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))[:50]

# retrieve the api key from storage
ACCESS_TOKEN = open(ROOT_DIR + "/keys/facebook_key.txt", 'r').read()

# specify api host and search path
API_HOST = 'https://graph.facebook.com'
SEARCH_PATH = '/v2.11/search'

# set up geocoder to convert city and state into coordinates
gn = geocoders.GeoNames(username='isaiahnields')

def request(host, path, url_params=None):
    """
    Given your API_KEY, send a GET request to the API.

    :param host: The domain host of the API.
    :param path: The path of the API after the domain.
    :param api_key: Your API Key.
    :param url_params: An optional set of query parameters in the request.
    :return dict: The JSON response from the request.
    :raise HTTPError: An error occurs from the HTTP request.
    """

    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))

    response = requests.request('GET', url, params=url_params)

    return response.json()

def search(term, location):
    """
    Given the business name and location, return the business information.

    :param term: the name of the business
    :param location: the location of the business
    :return request: the keys about the business of interest
    """

    # use geopy to get the coordinates from city and state information
    coordinates = gn.geocode(location)[1]
    center = str(coordinates[0]) + ',' + str(coordinates[1])

    # package the params into a dictionary
    params = {
        'type': 'place',
        'fields': 'name,category_list',
        'q': term,
        'center': center,
        'access_token': ACCESS_TOKEN
    }

    # make and return the request
    return request(API_HOST, SEARCH_PATH, params)

def get_category(term, location):
    """
    Given the business name and location, return the business name and category.

    :param term: the name of the business that should be searched
    :param location: the location of the business that should be searched
    :return result: an array containing the business name and category
    """

    try:
        result = search(term, location)
        return [result['keys'][0]['name'], result['keys'][0]['category_list'][0]['name']]
    except KeyError:
        return ['None', 'None']
    except IndexError:
        return ['None', 'None']
    except GeocoderTimedOut:
        return ['Timeout', 'Timeout']