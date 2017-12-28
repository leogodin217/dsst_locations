import requests
from bs4 import BeautifulSoup
import re

# Get the locations of testing centers
# type0 : 0 means don't look for schools that accept DSST
# type1 : 1 means look for places to perform the DSST tests
# type2 : 0 means don't look for Dantes fully-funded centers


def get_locations():

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

    request = requests.get(url, params=post_data)
    locations = []

    # Parse the response
    soup = BeautifulSoup(request.text, 'html.parser')
    raw_locations = soup.find_all('p', 'results')

    for location in raw_locations:
        # Get text/numbers/spaces before a new line
        details = re.findall(r'[aA-zZ0-9].+\n', location.text)
        # Different possible combinations here. Some locations have more lines
        # These are the most common.
        # [0] ID
        # [1] Name of institution
        # [2] address 1, but sometimes further name
        # [3] address 2, but sometimes address 1
        # [4] phone number, if available
        # [5] Link, if available.
        location_info = {}
        location_info['id'] = details[0].strip()
        location_info['name'] = details[1].strip()
        # Last line
        location_info['link'] = details[len(details) - 1].strip()
        # Second to last
        location_info['phone'] = details[len(details) - 2].strip()
        # Fourth from last holds street data
        location_info['Address'] = details[len(details) - 4].strip()
        # Third from last holds 'city, state zip'
        address2 = details[len(details) - 3].strip()
        city = re.match('[\w ]+', address2)
        state = re.search('\s+([A-Z][A-Z])', address2)
        zip_code = re.search('[0-9]+\s*$', address2)
        # re.search/match return None if no match. This allows us to use the
        # if statement and avoid errors.
        location_info['City'] = city.group(0) if city else city
        location_info['State'] = state.group(1) if state else state
        location_info['Zip'] = zip_code.group(0) if zip_code else zip_code
        # Add the record
        locations.append(location_info)
    return locations
