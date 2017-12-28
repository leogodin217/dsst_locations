from dsst_locations.location_parsing import parse_location


class TestLocationParsing:

    def setup_method(self):
        self.common_location = [
            '9397',
            'CHARTER COLLEGE',
            '2221 E. NORTHERN LIGHTS, SUITE 120',
            'ANCHORAGE, AK   99508',
            '907-777-1324',
            'http://chartercollege.edu/'
        ]

    def test_id_is_parsed(self):
        location = parse_location(self.common_location)
        location['id'].should.equal('9397')
