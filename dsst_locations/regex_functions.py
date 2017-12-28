''' Simple regex functions to capture links, email and other things
'''
import re


def is_phone_number(input):
    return re.match('\(?\d{3}[) -]{0,2}\d{3}[ -]?\d{4}', input)


def is_city_state_zip(input):
    return re.match('[\w ]+, [A-Z][A-Z] \d{5}', input)


def get_city(input):
    result = None
    match = re.match('^([\w ]+),', input)
    if match:
        result = match.groups()[0]
    return result


def get_state(input):
    result = None
    match = re.match('.+, ([A-Z][A-Z]) ', input)
    if match:
        result = match.groups()[0]
    return result


def get_zip_code(input):
    result = None
    match = re.search('\d{5}', input)
    if match:
        result = match.group()
    return result


def is_link(input):
    return re.match('^https?://', input)
