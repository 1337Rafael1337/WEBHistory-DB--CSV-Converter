
import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import pytz

def convert_time(edge_time, timezone_str='Europe/Berlin'):
    """Konvertiere die Edge-Zeitstempel in normale Datum/Uhrzeit."""
    # Erstelle ein naive datetime Objekt
    dt_naive = datetime(1601, 1, 1) + timedelta(microseconds=edge_time)
    # Definiere die ursprüngliche Zeitzone (UTC)
    utc_zone = pytz.timezone('UTC')
    # Mache das naive datetime-Objekt zu einem "aware" datetime-Objekt
    dt_aware = utc_zone.localize(dt_naive)
    # Definiere die Zielzeitzone
    target_zone = pytz.timezone(timezone_str)
    # Konvertiere das Datum in die Zielzeitzone
    return dt_aware.astimezone(target_zone)

def extract_history(db_path, output_csv_path):
    """Extrahiere den Browserverlauf aus der Edge-Datenbank und speichere ihn als CSV."""
    # Verbindung zur Edge History-Datenbank aufbauen
    conn = sqlite3.connect(db_path)
    
    # SQL-Query ausführen, um benötigte Daten zu erhalten
    query = """
    SELECT url, title, last_visit_time
    FROM urls
    """
    df = pd.read_sql_query(query, conn)
    
    # Konvertiere die last_visit_time in ein normales Datum mit Berücksichtigung der Zeitzone
    df['last_visit_time'] = df['last_visit_time'].apply(convert_time)
    
    # Ergebnisse in eine CSV-Datei speichern
    df.to_csv(output_csv_path, index=False)
    
    # Verbindung schließen
    conn.close()
    print(f'Daten wurden erfolgreich in {output_csv_path} gespeichert.')

# Pfad zur Datenbank und zum CSV-Ausgabeort
db_path = '/mnt/url/History'  # Pfad zur History-Datenbank anpassen
output_csv_path = '/home/rs/Dokumente/browser_history.csv'

# Funktion ausführen
extract_history(db_path, output_csv_path)
