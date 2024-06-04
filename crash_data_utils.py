# column_descriptions.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
# Define the column descriptions
column_descriptions = {
    'id': 'Unique identifier for each crash record.',
    'crash_date': 'Date of the crash.',
    'crash_time': 'Time of the crash.',
    'town': 'Town where the crash occurred.',
    'city': 'City where the crash occurred.',
    'state': 'State where the crash occurred.',
    'country': 'Country where the crash occurred.',
    'total_injured': 'Total number of injured individuals in the crash.',
    'total_killed': 'Total number of fatalities in the crash.',
    'injury_incapacitated': 'Number of incapacitating injuries in the crash.',
    'injury_non_incapacitated': 'Number of non-incapacitating injuries in the crash.',
    'most_severe_injury': 'The most severe injury reported in the crash.',
    'crash_type': 'Type of crash.',
    'contributory_cause': 'Primary cause of the crash.',
    'sec_contributory_cause': 'Secondary cause of the crash.',
    'num_vehicles_in_crash': 'Number of vehicles involved in the crash.',
    'crash_hit_and_run': 'Whether the crash was a hit-and-run.',
    'crash_severity': 'Severity of the crash.',
    'traffic_control_device': 'Traffic control device present at the crash location.',
    'traffic_control_device_condition': 'Condition of the traffic control device.',
    'road_defect': 'Any road defects at the crash location.',
    'lattitude': 'Latitude of the crash location.',
    'longitude': 'Longitude of the crash location.',
    'days_tempmax': 'Maximum temperature on the day of the crash.',
    'days_tempmin': 'Minimum temperature on the day of the crash.',
    'days_temp': 'Average temperature on the day of the crash.',
    'days_feelslikemax': 'Maximum "feels like" temperature on the day of the crash.',
    'days_feelslikemin': 'Minimum "feels like" temperature on the day of the crash.',
    'days_feelslike': '"Feels like" temperature on the day of the crash.',
    'days_dew': 'Dew point on the day of the crash.',
    'days_humidity': 'Humidity on the day of the crash.',
    'days_precip': 'Precipitation on the day of the crash.',
    'days_precipprob': 'Probability of precipitation on the day of the crash.',
    'days_precipcover': 'Precipitation cover on the day of the crash.',
    'days_preciptype': 'Type of precipitation on the day of the crash.',
    'days_snow': 'Snowfall on the day of the crash.',
    'days_snowdepth': 'Snow depth on the day of the crash.',
    'days_windgust': 'Wind gusts on the day of the crash.',
    'days_windspeed': 'Wind speed on the day of the crash.',
    'days_winddir': 'Wind direction on the day of the crash.',
    'days_pressure': 'Atmospheric pressure on the day of the crash.',
    'days_cloudcover': 'Cloud cover on the day of the crash.',
    'days_visibility': 'Visibility on the day of the crash.',
    'days_uvindex': 'UV index on the day of the crash.',
    'days_conditions': 'Weather conditions on the day of the crash.',
    'days_moonphase': 'Moon phase on the day of the crash.',
    'temp': 'Temperature at the time of the crash.',
    'feelslike': '"Feels like" temperature at the time of the crash.',
    'humidity': 'Humidity at the time of the crash.',
    'dew': 'Dew point at the time of the crash.',
    'precip': 'Precipitation at the time of the crash.',
    'precipprob': 'Probability of precipitation at the time of the crash.',
    'snow': 'Snowfall at the time of the crash.',
    'snowdepth': 'Snow depth at the time of the crash.',
    'precip_type': 'Type of precipitation at the time of the crash.',
    'windgust': 'Wind gusts at the time of the crash.',
    'windspeed': 'Wind speed at the time of the crash.',
    'winddir': 'Wind direction at the time of the crash.',
    'pressure': 'Atmospheric pressure at the time of the crash.',
    'visibility': 'Visibility at the time of the crash.',
    'cloudcover': 'Cloud cover at the time of the crash.',
    'conditions': 'Weather conditions at the time of the crash.',
    'sunrise': 'Time of sunrise on the day of the crash.',
    'sunset': 'Time of sunset on the day of the crash.',
    'moonphase': 'Moon phase at the time of the crash.'
}

# Create the summary DataFrame
summary = pd.DataFrame(list(column_descriptions.items()), columns=['Column Name', 'Description'])





