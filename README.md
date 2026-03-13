# Netflix Dashboard Data Analysis  

<rb>  

Dieses Projekt analysiert den Netflix‑Katalog anhand eines öffentlich verfügbaren Datensatzes.   
Ziel ist es, die wichtigsten Muster und Trends im globalen Content‑Portfolio sichtbar zu machen und ein   
professionelles Power BI Dashboard zu entwickeln, das Genres, Länder, Veröffentlichungsjahre und die Verteilung   
zwischen Filmen und Serien visualisiert.  

<br>  

## 📊 Projektübersicht  

Das Dashboard bietet einen klaren Überblick über:  

- **Top Genres** (Top 15, dynamisch berechnet)  
- **Content-Verteilung** zwischen Movies & TV Shows  
- **Anzahl der Titel pro Land**  
- **Entwicklung der Veröffentlichungen über die Jahre**  
- **Interaktive Filter** (Genre, Land, Release Year)  
- **KPI‑Karten** für Gesamtanzahl Titel, Movies, TV Shows und Länder  

Das Design folgt einem **Netflix‑Brand‑Look** mit dunklem Theme, roten Akzenten und klarer Typografie.  

<br>  

## 🛠️ Technologien & Tools  

- **Python (pandas)**    
  - Datenbereinigung    
  - Duplikate entfernen    
  - Datumsformate konvertieren  
  - Ableitung neuer Spalten (Added_Year)  

- **Power BI**  
  - Datenmodellierung  
  - DAX‑Measures (Top‑N, KPIs, dynamische Berechnungen)  
  - Dashboard‑Design im Netflix‑Style  
  - Interaktive Filter & Visuals  

<br>  

## 🧹 Datenbereinigung (Python)  

Die Rohdaten wurden mit Python aufbereitet:  

- Entfernen von Duplikaten  
- Vereinheitlichung der Spaltennamen  
- Konvertierung von `date_added` in ein Datumsformat  
- Ableitung der Spalte `Added_Year`  
- Export als `netflix_cleaned.csv` und `netflix_cleaned.xlsx`  
