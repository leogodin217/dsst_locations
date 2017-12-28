from ..regex_functions import is_phone_number
from ..regex_functions import is_city_state_zip
from ..regex_functions import is_link


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
            'A long town name, AZ 85142'
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
