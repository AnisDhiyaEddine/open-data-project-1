# parse world crime

import pandas as pd

data = pd.read_csv("datasets/World_Crime_Rate_Index_Per_Year_By_Country.csv")
years=["2013","2014","2015","2016","2017","2018","2019","2020","2021","2022"]

parsed=[]
for row in data.iterrows():
    c=row[1][0]
    for year in years:
        val=row[1][year]
        parsed.append([c, year, val])

HEADER = ["Country", "Year", "Crime Rate"]
frame = pd.DataFrame(data=parsed, columns=HEADER)
frame.to_csv("datasets/New_Wolrd_Crimes_Rate.csv")