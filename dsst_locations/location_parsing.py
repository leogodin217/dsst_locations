from dsst_locations.regex_functions import is_phone_number
from dsst_locations.regex_functions import is_city_state_zip
from dsst_locations.regex_functions import is_link


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
    location = {}
    location['id'] = location_items[0]
    # location['name'] = location_items[1]
    return location
