import requests
import urllib.request, json


def get_random_quote():
    '''Function that gets the json response to our quote url request'''
    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'.format()
    quote_data = requests.get(quote_url).json()
    print(quote_data)
    return quote_data


def get_quote():
    '''
    Function that gets the random quotes
    '''
    get_article_details_url = 'http://quotes.stormconsultancy.co.uk/random.json'.format()
    with urllib.request.urlopen(get_article_details_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)
        print(quote_response)
    return quote_response
