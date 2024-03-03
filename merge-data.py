import pandas as pd

musics=pd.read_csv("datasets/Favorite_Music_Genre_By_Country.csv")
crimes=pd.read_csv("datasets/New_Wolrd_Crimes_Rate.csv")
hapiness=pd.read_csv("datasets/World_Happiness_Index_Per_Year_By_Country.csv")

merged=pd.merge(crimes,musics,"left","Country")

file="resultats2013.csv"
cycle = pd.read_csv(file)
cycle["Country"] = cycle["Country"].map(lambda x: str(x).upper())

for i in range(2014,2024):
    file="resultats"+str(i)+".csv"
    data = pd.read_csv(file)
    data["Country"] = data["Country"].map(lambda x: str(x).upper())
    cycle=pd.concat([cycle, data])

merged=pd.merge(merged,cycle,"left",["Country", "Year"]).drop(columns=['Unnamed: 0'])
merged=pd.merge(hapiness, merged, "right",["Country", "Year"]).drop_duplicates()

merged.to_csv("merged.csv")