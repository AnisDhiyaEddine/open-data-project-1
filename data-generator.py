# Script to generate a data.csv file with 195 rows (countries) and 8 columns
# (ID, Country, Year, Type, Happiness Score, Happiness Rank, Daylight Duration, Crime Rate)

import csv
import random
import os
import pandas as pd
import numpy as np
import datetime

# Create a list of countries 'https://restcountries.eu/rest/v2/all'

# Fetch the data from the API
import json
import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
data = response.json()
countries = []
for i in range(len(data)):
    countries.append(data[i]['name']['common'])

years = [2015, 2016, 2017, 2018, 2019, 2020]

# music types
types = ['Rock', 'Pop', 'Jazz', 'Hip Hop', 'Rap', 'Country', 'Classical', 
         'Electronic', 'Folk', 'Reggae', 'Blues', 'Latin', 'Metal', 'Punk',
           'R&B', 'Soul', 'Funk', 'Disco', 'Techno', 'House', 'Ambient', 'Indie',
             'Alternative', 'Dance', 'Grunge', 'Gospel', 'Instrumental', 'Dubstep',
               'Trap', 'Ska', 'Salsa', 'Bachata', 'Merengue', 'Cumbia', 'Mariachi',
                 'Banda', 'Tejano', 'Ranchera', 'Bolero', 'Tango', 'Samba', 'Fado']


# happiness score
happiness_score = [random.uniform(0, 10) for i in range(6)]

# happiness rank
happiness_rank = [random.randint(1, 195) for i in range(6)]

# daylight duration
daylight_duration = [random.randint(0, 24) for i in range(6)]

# crime rate
crime_rate = [random.uniform(0, 10) for i in range(6)]

# Create a list of 195 IDs

ids = [i for i in range(195)]

# for each country construct random data for each year
data = []
for i in range(195):
    for j in range(random.randint(1, 6)):
        data.append([ids[i], 
                     countries[i], 
                     years[j], 
                     random.choice(types), 
                     happiness_score[j], 
                     happiness_rank[j], 
                     daylight_duration[j], 
                     crime_rate[j]])


# write the data to a csv file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Country", "Year", "Type", "Happiness Score", "Happiness Rank", "Daylight Duration", "Crime Rate"])
    writer.writerows(data)