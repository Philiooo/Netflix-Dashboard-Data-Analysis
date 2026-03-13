import pandas as pd
import os

#CSV laden
df = pd.read_csv("C:/Users/peich/Documents/Projekt/Netflix/archive (2)/netflix_titles.csv")


#Überblick über die Daten
print(df.info())
print(df.head())

#Datenbereinigung
#Duplikate entfernen
df = df.drop_duplicates()

# Fehlende Werte markieren
missing = df.isnull().sum()
print("Fehlende Werte pro Spalte:\n", missing)

#Spaltennamen vereinfachen 
df.rename(columns={
    'show_id': 'ID',
    'type': 'Type',
    'title': 'Title',
    'director': 'Director',
    'cast': 'Cast',
    'country': 'Country',
    'date_added': 'Date_Added',
    'release_year': 'Release_Year',
    'rating': 'Rating',
    'duration': 'Duration',
    'listed_in': 'Genres',
    'description': 'Description'
}, inplace=True)

#Neue Spalten ableiten
df['Date_Added'] = pd.to_datetime(df['Date_Added'], errors='coerce')
df['Added_Year'] = df['Date_Added'].dt.year

#Erste Analysen vorbereiten
#Top 10 Genres
top_genres = df['Genres'].value_counts().head(10)
print("Top 10 Genres:\n", top_genres)

#Anzahl Inhalte pro Jahr
content_per_year = df['Release_Year'].value_counts().sort_index()
print("Content pro Jahr:\n", content_per_year)

#Movies vs TV Shows
type_count = df['Type'].value_counts()
print("Movies vs TV Shows:\n", type_count)

#Ergebnisse als Excel speichern
excel_path = "C:/Users/peich/Documents/Projekt/Netflix/netflix_cleaned.xlsx"
df.to_excel(excel_path, index=False)
print(f"Bereinigte Excel-Datei gespeichert: {excel_path}")

#Excel-Datei automatisch öffnen (Windows)
os.startfile(excel_path)
