import requests
import os
from urllib.parse import quote

# Yelp Fusion no longer uses OAuth as of December 7, 2017.
# You no longer need to provide Client ID to fetch Data
# It now uses private keys to authenticate requests (API Key)
# You can find it on
# https://www.yelp.com/developers/v3/manage_app


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))[:50]
API_KEY = open(ROOT_DIR + "/keys/yelp_key.txt", 'r').read()

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 1


def request(host, path, api_key, url_params=None):
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
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(term, location):
    """
    Query the Search API by a search term and location.

    :param term: The search term passed to the API.
    :param location: The search location passed to the API.
    :return dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params)


def get_category(term, location):
    """
    Query the Business API by a business ID.

    :param term: the name of the business that should be searched
    :param location: the location of the business that should be searched
    :return result: an array of the business name with its result
    """

    try:
        result = search(term, location)
        return [result['businesses'][0]['name'], result['businesses'][0]['categories'][0]['title']]
    except KeyError:
        return ['None', 'None']
    except IndexError:
        return ['None', 'None']
