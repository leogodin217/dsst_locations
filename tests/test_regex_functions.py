from dsst_locations.regex_functions import is_phone_number
from dsst_locations.regex_functions import is_city_state_zip
from dsst_locations.regex_functions import is_link
from dsst_locations.regex_functions import get_city
from dsst_locations.regex_functions import get_state
from dsst_locations.regex_functions import get_zip_code
from dsst_locations.regex_functions import is_street_address


class TestPhoneNumbers:

    def test_real_phone_numbers(self):
        phone_numbers = [
            '(999) 222 3333',
            '(999)-222 3333',
            '9992223333',
            '999 222-3333',
            '999-222-3333',
            '999-222 3333',
            '999-222-3333 x 4222'
        ]
        for phone_number in phone_numbers:
            match = is_phone_number(phone_number)
            if match:
                match.string.should.equal(phone_number)
            else:
                # This is actually false, but shows the missed phone number
                match.should.equal(phone_number)

    def test_bad_phone_numbers(self):
        phone_numbers = [
            '(999) 222 333',
            '(999)-22 3333',
            '999223333',
            '223 something road 3333',
        ]
        for phone_number in phone_numbers:
            match = is_phone_number(phone_number)
            if match:
                match.string.should.be.false
            else:
                match.should.be.false

    def test_real_city_state_zip(self):
        addresses = [
            'Auburn, CA 95603',
            'New Ipswich, NH 03071',
            'New Ipswich, NH 03071-0124',
            'A long town name, AZ 85142',
            'with extra spaces,   AZ   44444',
            'ST. PAUL, MN 55112',
            'FT. LEWIS, WA 98433'
        ]
        for address in addresses:
            match = is_city_state_zip(address)
            if match:
                match.string.should.equal(address)
            else:
                # This is actually false, but shows the missed address
                match.should.equal(address)

    def test_bad_city_state_zip(self):
        addresses = [
            'No testting on Thursdays, our rules',
            'Wednexday, Thursday, Friday',
            'Only for students',
            'http://something.com, ON Tuesday'
        ]
        for address in addresses:
            match = is_city_state_zip(address)
            if match:
                # Should not be a match, but this gives us the line that failed
                match.string.should.be.false
            else:
                match.should.be.false

    def test_is_link(self):
        links = [
            'http://example.com',
            'https://example.com/somaapp/somerest/someresource/1'
        ]

        for link in links:
            match = is_link(link)
            if match:
                match.string.should.equal(link)
            else:
                # Should not happen, but this shows us the missed link
                match.should.equal(link)

    def test_can_get_city(self):
        line = 'Auburn, CA 95603'
        get_city(line).should.equal('Auburn')

    def test_can_get_long_city(self):
        line = 'Some long city, CA 95603'
        get_city(line).should.equal('Some long city')

    def test_can_get_city_with_dot(self):
        line = 'ST. PAUL, MN 55112'
        get_city(line).should.equal('ST. PAUL')

    def test_can_get_state(self):
        line = 'Some long city, CA 95603'
        get_state(line).should.equal('CA')

    def test_can_get_zip_code(self):
        line = 'Some long city, CA 95603'
        get_zip_code(line).should.equal('95603')

    def test_good_street_addresses(self):
        lines = [
            '100 some streen',
            '204 street 1 building 14',
            '5000 W. Something way office 201'
        ]
        for line in lines:
            match = is_street_address(line)
            if match:
                match.string.should.equal(line)
            else:
                # Should not happen, but this will show what we missed
                match.should.equal(line)

    def test_bad_street_address(self):
        lines = [
            'Testing on Thursdays',
            'Only our students 100',
            '2pm - 4pm'
        ]
        for line in lines:
            match = is_street_address(line)
            if match:
                # Should not happen, but this will show what we missed
                match.string.should.be.false
            else:
                match.should.be.false