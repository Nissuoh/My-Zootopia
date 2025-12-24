import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'

    if 'name' in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get('characteristics', {})

    if 'diet' in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if 'locations' in animal_obj and len(animal_obj['locations']) > 0:
        output += f'      <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if 'type' in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    animals_data = load_data('animal_data.json')

    animals_html = ''
    for animal_obj in animals_data:
        animals_html += serialize_animal(animal_obj)

    with open("animal_template.html", "r") as f:
        template_content = f.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Projekt erfolgreich abgeschlossen: 'animals.html' wurde generiert.")


if __name__ == "__main__":
    main()