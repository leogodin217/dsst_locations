''' Simple regex functions to capture links, email and other things
'''
import re


def is_phone_number(input):
    return re.match('\(?\d{3}[) -]{0,2}\d{3}[ -]?\d{4}', input)


def is_city_state_zip(input):
    return re.match('[\w ]+, [A-Z][A-Z] \d{5}', input)


def is_link(input):
    return re.match('^https?://', input) 
