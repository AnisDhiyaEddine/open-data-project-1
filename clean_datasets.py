import pandas as pd
import os

csv_music = './datasets/Favorite_Music_Genre_By_Country.csv'
csv_crime = './datasets/World_Crime_Rate_Index_Per_Year_By_Country.csv'
csv_happiness = './datasets/World_Happiness_Index_Per_Year_By_Country.csv'

def process_csv(df, file_name):
    df['Country'] = df['Country'].str.upper()
    
    df.replace('..', float('nan'), inplace=True)
    df.to_csv(file_name, index=False)

def filter_rows(file, countries_list):
    df = pd.read_csv(file)
    if 'Country' in df.columns:
        df_filtered = df[df['Country'].str.upper().isin(countries_list)]
        return df_filtered
    else:
        print(f"Skipping dataset as it does not contain 'Country' column.")

datasets = [csv_music, csv_crime, csv_happiness]
print("Starting processing files...")

dataset_music_genre = pd.read_csv(csv_music)
country_list = dataset_music_genre['Country'].str.upper().tolist()

for dataset in datasets:
    filtered_df = filter_rows(dataset, country_list)
    if filtered_df is not None:
        process_csv(filtered_df, dataset) 

print("Processing completed successfully!")
