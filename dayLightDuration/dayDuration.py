import requests
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Charger les données du fichier CSV initial
df = pd.read_csv('dayLightDuration/country-capital-lat-long-population.csv')

# Fonction pour convertir la durée en secondes
def convertir_en_secondes(duree):
    heures, minutes, secondes = map(int, duree.split(':'))
    return heures * 3600 + minutes * 60 + secondes

# Fonction pour convertir les secondes en durée lisible
def convertir_en_duree(secondes):
    duree = timedelta(seconds=secondes)
    heures, remainder = divmod(duree.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(heures, minutes, seconds)

# Créer un dataframe pour stocker les résultats
resultats = pd.DataFrame(columns=['Country', 'Year', 'Month', 'Day_Length', 'Sunrise', 'Sunset'])

# Date de début et fin
date_debut = datetime(2018, 1, 1)
date_fin = datetime(2019, 1, 1)

try:
    # Boucle sur chaque ligne du dataframe
    for index, row in df.iterrows():
        pays = row['Country'].replace(' ', '_')
        latitude = row['Latitude']
        longitude = row['Longitude']

        # Boucle sur chaque mois entre 2013 et 2024
        date_actuelle = date_debut
        while date_actuelle < date_fin:
            # Effectuer la requête à l'API Sunrise-Sunset
            url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={date_actuelle.strftime("%Y-%m-%d")}'
            response = requests.get(url)
            data = response.json()

            # Extraire les informations de lever et de coucher du soleil
            sunrise = data['results']['sunrise']
            sunset = data['results']['sunset']
            day_length = data['results']['day_length']

            # Ajouter les résultats au dataframe
            resultats = resultats._append({
                'Country': pays,
                'Year': date_actuelle.year,
                'Month': date_actuelle.month,
                'Day_Length': day_length,
                'Sunrise': sunrise,
                'Sunset': sunset,
            }, ignore_index=True)
            print(resultats)
            # Passer au mois suivant
            date_actuelle += relativedelta(months=1)

except Exception as e:
    print(f"Une erreur s'est produite : {e}")

finally:
    # Convertir la colonne 'Day_Length' en secondes
    resultats['Day_Length_Seconds'] = resultats['Day_Length'].apply(convertir_en_secondes)

    # Enregistrer les résultats dans un fichier CSV
    resultats.to_csv('resultats_sunrise_sunset2023.csv', index=False)

    # Grouper par année et par pays, puis calculer la moyenne des durées du jour
    averages = resultats.groupby(['Year', 'Country'])['Day_Length_Seconds'].mean().reset_index()
    averages['Average_Day_Length'] = averages['Day_Length_Seconds'].apply(convertir_en_duree)

    # Écrire les résultats dans un nouveau fichier CSV
    output_file = 'resultats2018.csv'
    averages[['Year', 'Country', 'Average_Day_Length']].to_csv(output_file, index=False)

    print(f"Les résultats ont été enregistrés dans {output_file}.")
