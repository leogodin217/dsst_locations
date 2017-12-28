import requests
from bs4 import BeautifulSoup

# Get the locations of testing centers
# type0 : 0 means don't look for schools that accept DSST
# type1 : 1 means look for places to perform the DSST tests
# type2 : 0 means don't look for Dantes fully-funded centers


def get_data():

    url = 'http://getcollegecredit.com/cgi-bin/DxR_GCC/search_print.pl'
    post_data = {
        'preview': '0',
        'action': 'search',
        'search_string': '',
        'state_select': 'STATES',
        'type0': '0',
        'type1': '1',
        'type2': '0',
        'urlid': 'OwSwkWBYiYjlUeCSF7rtV5BfcLoyba0Z'
    }

    return requests.get(url, params=post_data)


def get_locations_from_raw_data(raw_data):
    # raw_data: text result from a requests get
    # Each location is contained within a <p> tag
    # Each detail in a locaiton precedes a <br /> 
    # There are no classes or IDs that tag parts of a location
    # We do not know what is a phone number, city, state, address, etc...

    locations = []
    soup = BeautifulSoup(raw_data, 'html.parser')
    # All paragraphs contain exactly one location
    raw_locations = soup.find_all('p', 'results')
    for location in raw_locations:
        locations.append([location for location in location.stripped_strings])
    return locations
