from get_dsst_locations import get_data, get_locations_from_raw_data
from location_parsing import parse_location
from datetime import datetime
import math
import pandas as pd

# Quick run script to pull data, parse it and save to CSV

# get_data connects to the DSST site and pulls HTML for all locations. Returns
# a requests.models.Response
data = get_data()
locations = []
if data.status_code == 200:
    # Turn HTML to a list of data items
    locations = get_locations_from_raw_data(data.text)

#  parse the data and save it to a list of dicts
location_data = [parse_location(location) for location in locations]

# save the data as CSV
timestamp = math.floor(datetime.now().timestamp())
file_name = f'../data/dsst_locations_{timestamp}.csv'
location_frame = pd.DataFrame(location_data)
location_frame.to_csv(file_name)
