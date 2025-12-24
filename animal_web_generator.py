import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data('animal_data.json')

    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">\n'

        if 'name' in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        output += '  <p class="card__text">\n'

        if 'characteristics' in animal:
            if 'diet' in animal['characteristics']:
                output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

            if 'locations' in animal and len(animal['locations']) > 0:
                output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

            if 'type' in animal['characteristics']:
                output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    with open("animal_template.html", "r") as f:
        template_content = f.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Glückwunsch! Schritt 4 abgeschlossen. 'animals.html' ist nun fertig gestaltet.")


if __name__ == "__main__":
    main()
