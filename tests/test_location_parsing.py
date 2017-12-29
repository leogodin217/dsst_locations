from dsst_locations.location_parsing import parse_location


class TestLocationParsing:

    def setup_method(self):
        common_location = [
            '9397',
            'CHARTER COLLEGE',
            '2221 E. NORTHERN LIGHTS, SUITE 120',
            'ANCHORAGE, AK   99508',
            '907-777-1234',
            'http://chartercollege.edu/'
        ]
        self.common_parsed = parse_location(common_location.copy())

    def test_id_is_parsed(self):
        self.common_parsed['id'].should.equal('9397')

    def test_name_is_parsed(self):
        self.common_parsed['name'].should.equal('CHARTER COLLEGE')

    def test_link_is_parsed(self):
        self.common_parsed['links'].should.equal(
            ['http://chartercollege.edu/'])

    def test_city_is_parsed(self):
        self.common_parsed['city'].should.equal('ANCHORAGE')

    def test_state_is_parsed(self):
        self.common_parsed['state'].should.equal('AK')

    def test_zip_code_is_parsed(self):
        self.common_parsed['zip_code'].should.equal('99508')

    def test_street_address_is_parsed(self):
        self.common_parsed['street_address'].should.equal(
            '2221 E. NORTHERN LIGHTS, SUITE 120')

    def test_phone_number_is_parsed(self):
        self.common_parsed['phone_numbers'].should.equal(['907-777-1234'])

    def test_multiple_links(self):
        location = [
            '9397',
            'CHARTER COLLEGE',
            '2221 E. NORTHERN LIGHTS, SUITE 120',
            'ANCHORAGE, AK   99508',
            '907-777-1234',
            'http://chartercollege.edu/',
            'https://chartercollege.edu/'
        ]
        parsed = parse_location(location)
        expected_links = [
            'http://chartercollege.edu/',
            'https://chartercollege.edu/']
        parsed['links'].should.equal(expected_links)

    def test_multiple_phone_numbers(self):
        location = [
            '9397',
            'CHARTER COLLEGE',
            '2221 E. NORTHERN LIGHTS, SUITE 120',
            'ANCHORAGE, AK   99508',
            '907-777-1234',
            '907-777-1235',
            'https://chartercollege.edu/'
        ]
        parsed = parse_location(location)
        expected_phone_numbers = [
            '907-777-1234',
            '907-777-1235'
        ]
        parsed['phone_numbers'].should.equal(expected_phone_numbers)

    # Specific entries that have failed to parse #
    def test_st_paul_mn(self):
        location = [
            '8060',
            'UNIVERSITY OF NORTHWESTERN - ST. PAUL',
            'FOCUS, 3003 SNELLING AVENUE NORTH',
            'ST. PAUL, MN   55113',
            '651-631-5263',
            'http://www.unwsp.edu'
        ]
        parsed = parse_location(location)
        parsed['city'].should.equal('ST. PAUL')

    def test_no_readable_address(self):
        location = [
            '9798',
            'NORTHWEST ARKANSAS COMMUNITY COLLEGE',
            'ONE COLLEGE DRIVE',
            'STUDENT CENTER 306',
            'BENTONVILLE, AR   72712',
            '(479) 986-4078',
            'http://www.nwacc.edu/'
        ]
        parsed = parse_location(location)
        parsed['street_address'].should.equal(
            'NORTHWEST ARKANSAS COMMUNITY COLLEGE')
