from dsst_locations.regex_functions import is_phone_number
from dsst_locations.regex_functions import is_city_state_zip
from dsst_locations.regex_functions import is_link
from dsst_locations.regex_functions import get_city
from dsst_locations.regex_functions import get_state
from dsst_locations.regex_functions import get_zip_code
from dsst_locations.regex_functions import is_street_address


def parse_location(location_items):
    """ location_items is a list of all the items we pulled about a location
    since there is no metadata telling us what each line represents, we need
    to make assupmptions and guesses.
    location_items[0] is always the ID of the location
    location_items[1] is always the name of the location
    If links exist, they will always be at the end of the list
    If phone numbers exist, they will always immediately precede links
    City, state, zip will always immediately precede phone numbers and links
    The line prededing City, state, zip may be an address or a random comment
    The line following name may be an address or a random comment.
    """
    # Set blank defaults for the items
    location = {
        'id': '',
        'name': '',
        'links': [],
        'city': '',
        'state': '',
        'zip_code': '',
        'street_address': ''
    }
    location['id'] = location_items[0]
    location['name'] = location_items[1]
    del location_items[0:2]  # Don't need these anymore

    # Start an index of items we should delete before finding the street
    # address
    delete_items = []

    # Delete list is used to remove items from location_details, after we
    # do not need them.
    # get links
    links = []
    for index, value in enumerate(location_items):
        if is_link(value):
            links.append(value)
            delete_items.append(index)

    location['links'] = links

    # Get phone numbers
    phone_numbers = []
    for index, value in enumerate(location_items):
        if is_phone_number(value):
            phone_numbers.append(value)
            delete_items.append(index)
    location['phone_numbers'] = phone_numbers

    # Get city, state, zip
    # Since we've removed links and phone numbers the last item in the list
    # should contain this line. However, some locations have random text
    # where links and phone numbers should be. To handle this, we will
    # use a regex to find a city, state zip line
    for index, value in enumerate(location_items):
        if is_city_state_zip(value):
            location['city'] = get_city(value)
            location['state'] = get_state(value)
            location['zip_code'] = get_zip_code(value)
            delete_items.append(index)

    # Delete everything we have used so far. This simplifies what we are doing
    # in finding the street address

    # Sort and reverse, so we can delete the last items first. Otherwise, we
    # will delete early items and reset numbering
    delete_items.sort()
    delete_items.reverse()
    for item in delete_items:
        del location_items[item]

    # Deleate everything we have used so far
    # Get street address
    # If there is only one line, we assume it is the street address
    # this is the most common case. If there are more than one, then
    # we will look for a number followed by some words
    if len(location_items) == 1:
        location['street_address'] = location_items[0]
    else:
        for item in location_items:
            if is_street_address(item):
                location['street_address'] = item
    # When all else fails, use the college name. That should work most of
    # the time
    if location['street_address'] == '':
        location['street_address'] = location['name']

    return location
