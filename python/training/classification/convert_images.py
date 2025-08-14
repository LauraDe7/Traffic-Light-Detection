print("Script startet")


import os

from PIL import Image

# Hier den Pfad zu deinen Originalbildern (relativ zum Skriptordner)
source_folder = 'traffic_lights_all/yellow'

# Hier der Zielordner für die konvertierten Bilder (wird automatisch erstellt)
target_folder = 'traffic_lights_all_jpg/yellow'

# Falls Zielordner noch nicht existiert, erstellen
os.makedirs(target_folder, exist_ok=True)

# Alle Dateien im source_folder durchgehen
for filename in os.listdir(source_folder):
    # Voller Pfad zur Quelldatei
    source_path = os.path.join(source_folder, filename)

    # Dateiname ohne Endung + neue Endung .jpg
    base_name = os.path.splitext(filename)[0]
    target_path = os.path.join(target_folder, base_name + '.jpg')

    try:
        # Bild öffnen
        with Image.open(source_path) as img:
            # In RGB konvertieren (wichtig, sonst Fehler bei manchen Formaten)
            rgb_img = img.convert('RGB')
            # Als jpg speichern
            rgb_img.save(target_path, 'JPEG')
        print(f'Converted {filename} -> {base_name}.jpg')
    except Exception as e:
        print(f'Fehler bei {filename}: {e}')

        

