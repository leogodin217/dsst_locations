from dsst_locations.get_dsst_locations import get_locations_from_raw_data
from dsst_locations.get_dsst_locations import get_new_locations
from dsst_locations.get_dsst_locations import get_deleted_locations


class TestGetDSSTLocations:

    def setup_method(self):
        # Taken from real data
        self.raw_locations = """
        <p class="region">ALASKA</p>
            <div id="liveResults">
                <div id="resultsLeft">
                    <p class="results">
                    9397<br />
                    CHARTER COLLEGE<br />
                    2221 E. NORTHERN LIGHTS, SUITE 120<br />
                    ANCHORAGE, AK   99508<br />
                    907-777-1324<br />
                    <a href="http://chartercollege.edu/" target="_blank" title="Opens in new window" class="externallink">http://chartercollege.edu/</a><br />
                    </p>
                </div>
                <div id="resultsRight">
                    <strong>This Location:</strong>
                    <ul class="options">
                            <li class="options" style="text-indent: -22px;">Awards credit for DSST exams.</li>
                                    <li class="options" style="text-indent: -22px;">Delivers Internet-based exams.</li>
                    </ul>
                </div>
                <div style="clear:both;height:10px;"></div>
            </div>
            <div id="liveResults">
                <div id="resultsLeft">
                    <p class="results">
                    8139<br />
                    KENAI PENINSULA COLLEGE<br />
                    156 COLLEGE ROAD<br />
                    SOLDOTNA, AK   99669<br />
                    (907) 262-0327<br />
                    <a href="http://www.kpc.alaska.edu/kpc/" target="_blank" title="Opens in new window" class="externallink">http://www.kpc.alaska.edu/kpc/</a><br />
                    </p>
                </div>
                <div id="resultsRight">
                    <strong>This Location:</strong>
                    <ul class="options">
                            <li class="options" style="text-indent: -22px;">Awards credit for DSST exams.</li>
                                <li class="options" style="text-indent: -22px;">Delivers paper-based exams.</li>
                            <li class="options" style="text-indent: -22px;">DANTES Fully-Funded military test center.</li>
                    </ul>
                </div>
                <div style="clear:both;height:10px;"></div>
            </div>
        """

    def test_get_locations_from_raw_data(self):
        # Two locations, each with six lines of data
        locations = get_locations_from_raw_data(self.raw_locations)
        locations.should.have.length_of(2)
        locations[0].should.have.length_of(6)
        locations[1].should.have.length_of(6)

    def test_get_new_locations(self):
        existing_location_ids = ['1111', '2222', '3333']
        locations = [
            ['0000', 'biz'],
            ['1111', 'foo'],
            ['2222', 'bar'],
            ['3333', 'baz'],
            ['4444', 'buz']
        ]
        new_locations = get_new_locations(existing_location_ids, locations)
        new_locations.should.equal([['0000', 'biz'], ['4444', 'buz']])

    def test_get_deleted_locations(self):
        existing_location_ids = ['1111', '2222', '3333', '4444']
        locations = [
            ['1111', 'foo'],
            ['3333', 'baz'],
        ]
        deleted_locations = get_deleted_locations(
            existing_location_ids, locations)
        deleted_locations.should.equal(['2222', '4444'])
