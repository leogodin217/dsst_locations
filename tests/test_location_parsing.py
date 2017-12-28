from dsst_locations.location_parsing import parse_location


class TestLocationParsing:

    def setup_method(self):
        common_location = [
            '9397',
            'CHARTER COLLEGE',
            '2221 E. NORTHERN LIGHTS, SUITE 120',
            'ANCHORAGE, AK   99508',
            '907-777-1324',
            'http://chartercollege.edu/'
        ]
        self.common_parsed = parse_location(common_location.copy())

    def test_id_is_parsed(self):
        self.common_parsed['id'].should.equal('9397')

    def test_name_is_parsed(self):
        self.common_parsed['name'].should.equal('CHARTER COLLEGE')

    def test_link_is_parsed(self):
        self.common_parsed['links'].should.equal(['http://chartercollege.edu/'])

    # def test_city_is_parsed(self):
    #     self.common_parsed['city'].should.equal('ANCHORAGE')

    # def test_state_is_parsed(self):
    #     self.common_parsed['state'].should.equal('AK')

    # def test_zip_code_is_parsed(self):
    #     self.common_parsed['zip_code'].should.equal('99508')
