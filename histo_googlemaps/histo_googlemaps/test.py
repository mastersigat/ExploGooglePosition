import pandas as pd
import json

# Charger le fichier JSON
with open("Takeout\Historique des positions (Vos trajets)\Records.json") as f:
    data = json.load(f)

# Transformer les données en DataFrame
locations = pd.DataFrame(data["locations"])

# Calculer les coordonnées en latitude et longitude
locations["lat"] = locations["latitudeE7"] / 1e7
locations["lon"] = locations["longitudeE7"] / 1e7

# Sélectionner les colonnes nécessaires
Historiquedepositions = locations[["timestamp", "deviceTag", "source", "lat", "lon"]]

# Renommer les colonnes
Historiquedepositions.columns = ["timestamp", "dispositif", "source", "lat", "lon"]

# Enregistrer en CSV
Historiquedepositions.to_csv('Historiquedepositions.csv', index=False)
HistoriqueOK = 'Historiquedepositions.csv'


