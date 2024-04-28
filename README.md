# WEBHistory_DB__CSV_Converter

## Projektbeschreibung
Dieses Repository enthält das Python-Skript `WEBHistory_DB__CSV_Converter.py`, das entwickelt wurde, um den Browserverlauf aus einer Edge-Browser-Datenbank zu extrahieren und diesen in eine CSV-Datei zu konvertieren. Es unterstützt die Konvertierung von Zeitstempeln, die speziell seit dem 1. Januar 1601 formatiert sind, in ein menschenlesbares Datum unter Berücksichtigung einer definierten Zeitzone.

## Funktionalitäten
- **Extraktion von URL, Titel und Besuchszeit** aus der Edge-Browser-Datenbank.
- **Konvertierung der `last_visit_time`** in das lokale Datum/Zeit unter Verwendung einer angegebenen Zeitzone.
- **Speichern der extrahierten Daten als CSV-Datei.**

## Voraussetzungen
- Python 3.x
- Bibliotheken: `sqlite3`, `pandas`, `pytz`

## Installation
Um die benötigten Bibliotheken zu installieren, führen Sie folgenden Befehl aus:
```bash
pip install pandas pytz
