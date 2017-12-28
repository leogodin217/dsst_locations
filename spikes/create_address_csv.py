from data import get_locations
import pandas as pd

# Pull DSST testing locations and save the addresses to a CSV.
# This CSV will be used to batch geolocate the addresses. 
locations = get_locations()
locations_frame = pd.DataFrame(locations)
locations_frame.to_csv('dsst-locations.csv', index=False)
