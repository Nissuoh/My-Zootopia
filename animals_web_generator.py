import json


def load_data(file_path):
    """
    Lädt die Tierdaten aus einer JSON-Datei.
    Behandelt Fehler für fehlende Dateien oder ungültiges JSON.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{file_path}' wurde nicht gefunden.")
        return []
    except json.JSONDecodeError:
        print(f"Fehler: Die Datei '{file_path}' enthält kein gültiges JSON.")
        return []


def read_template(file_path):
    """
    Liest die HTML-Vorlagendatei ein.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fehler: Das Template '{file_path}' wurde nicht gefunden.")
        return ""


def serialize_animal(animal_obj):
    """
    Wandelt ein Tier-Objekt in ein HTML-Listen-Element um.
    Nutzt .get() für sicheren Zugriff auf die Datenfelder.
    """
    name = animal_obj.get('name')
    char = animal_obj.get('characteristics', {})
    locs = animal_obj.get('locations', [])

    output = '<li class="cards__item">\n'
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <div class="card__text">\n    <ul class="animal-details">\n'

    attributes = {
        "Diet": char.get('diet'),
        "Location": locs[0] if locs else None,
        "Type": char.get('type'),
        "Skin Type": char.get('skin_type')
    }

    for label, value in attributes.items():
        if value:
            output += f"      <li><strong>{label}:</strong> {value}</li>\n"

    output += '    </ul>\n  </div>\n</li>\n'
    return output


def write_output(file_path, content):
    """
    Schreibt den generierten HTML-Inhalt in die Zieldatei.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Datei erfolgreich erstellt: {file_path}")
    except IOError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")


def main():
    """
    Hauptsteuerung: Lädt Daten, generiert HTML und speichert die Datei.
    """
    data = load_data('animals_data.json')
    if not data:
        return

    template = read_template('animals_template.html')
    if not template:
        return

    animals_html = ""
    for animal in data:
        animals_html += serialize_animal(animal)

    final_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    write_output("animals.html", final_content)


if __name__ == "__main__":
    main()
