# Zeittabelle für Arbeitszeitdaten erstellen

Python-Skript zur Erstellung formatierter Excel-Zeittabellen aus Arbeitszeitdaten mit automatischer deutscher Feiertagsintegration.

## 📋 Vorbereitung

Bevor das Skript ausgeführt wird, müssen die folgenden Schritte durchgeführt werden:

### 1. Zeitdaten anfordern
Sende eine E-Mail mit dem Betreff **"STATUS"** um Arbeitszeitdaten anzufordern.

### 2. Daten in JSON-Format übertragen
Übertrage die erhaltenen Zeitdaten in das JSON-Format. Die Daten müssen wie folgt aussehen:

**Dies ist ein Tag, deine Daten haben wahrscheinlich mehrere Tage.**
```json
[
  {
    "date": "2026-01-06",
    "weekday": "Dienstag",
    "status": "A",
    "status_label": "Anwesend",
    "start_time": "08:00",
    "end_time": "16:30",
    "duration_minutes": 480,
    "duration": "08:00",
    "punch_count": 2,
    "break_minutes": 30,
    "fallback_end_applied": false
  }
]
```

### 3. Datei im Input-Ordner hinterlegen
Speichern Sie die erstellte `data.json` Datei im `/input` Ordner.

## 📋 Anforderungen

### Benötigte Pakete
```bash
pip install openpyxl requests
```
### alternativ

```bash
python pip install -r requirements.txt
```
__________
### Erforderliche Verzeichnisse / Dateien
```
Zeitnachweis/
            ├── input/
            │           └── data.json
            ├── templates/
            │           └── template.xlsx
            └── scripts/
                        ├── create_basic_headers.py
                        ├── create_work_day_from_dict.py
                        ├── export_with_holidays.py
                        ├── fetch_holidays.py
                        ├── fill_holidays.py
                        ├── find_template_sheet.py
                        ├── get_file_extension.py
                        ├── get_german_holidays.py
                        ├── get_status_label.py
                        ├── handle_validation_error.py
                        ├── load_json_data.py
                        ├── load_work_data.py
                        ├── process_work_day_data.py
                        ├── start_time_export.py
                        ├── update_sheet_dates.py
                        ├── validate_file_path.py
                        ├── validate_paths.py
                        ├── write_work_data.py
                        └── WorkDay.py

```

## 🚀 Schnellstart

### Nach Excel exportieren
```bash
# Standard (Niedersachsen)
python start_time_export.py

# Bestimmtes Bundesland
python start_time_export.py BY

# Benutzerdefinierte Zeitdaten-Datei
python start_time_export.py NI ../input/my_data.json
```

## 🎯 Statuscodes

| Code | 
|------|
| ANWESEND |
| URLAUB |
| KRANK |
| KIND_KRANK | 
| SCHULE | 
| FREI_FEIERTAG | 
| FEIERTAG_AUTO | 
| ENTSCHULDIGT | 
| PRAKTIKUM_NICHT_BEGONNEN | 
| FERTIG | 
| UNBEKANNT | 
| KEIN_EINTRAG | 

## 🇩🇪 Bundeslandcodes

| Code | Bundesland |
|------|------------|
| BY | Bayern |
| BW | Baden-Württemberg |
| BE | Berlin |
| BB | Brandenburg |
| HB | Bremen |
| HH | Hamburg |
| HE | Hessen |
| MV | Mecklenburg-Vorpommern |
| NI | Niedersachsen |
| NW | Nordrhein-Westfalen |
| RP | Rheinland-Pfalz |
| SL | Saarland |
| SN | Sachsen |
| ST | Sachsen-Anhalt |
| SH | Schleswig-Holstein |
| TH | Thüringen |

## 📁 Ausgabe

Erstellt separate Excel-Dateien für jeden Monat:
```
ZEITNACHWEIS_2026_1.xlsx  (Januar 2026)
ZEITNACHWEIS_2026_2.xlsx  (Februar 2026)
...
```

## ⚙️ Kommandozeilenargumente
1. **Zum Ordner navigieren:**
```bash
cd ./Zeitnachweis/scripts
```

2. **Skript ausführen:**
```bash
python start_time_export.py [state_code] [data_file] [--input-dir DIR] [--output-dir DIR]
```

- `state_code`: Bundesland für Feiertage (optional, Standard: NI)
- `data_file`: Pfad zur JSON-Datendatei (optional)
- `--input-dir`: Input-Verzeichnis (optional, Standard: ../input)
- `--output-dir`: Output-Verzeichnis (optional, Standard: ../output)
