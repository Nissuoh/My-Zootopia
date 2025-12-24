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
            output += f"    Name: {animal['name']}<br/>\n"

        if 'characteristics' in animal:
            if 'diet' in animal['characteristics']:
                output += f"    Diet: {animal['characteristics']['diet']}<br/>\n"

            if 'locations' in animal and len(animal['locations']) > 0:
                output += f"    Location: {animal['locations'][0]}<br/>\n"

            if 'type' in animal['characteristics']:
                output += f"    Type: {animal['characteristics']['type']}<br/>\n"

        output += '</li>\n'

    with open("animal_template.html", "r") as f:
        template_content = f.read()

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as f:
        f.write(new_html_content)

    print("Schritt 3 abgeschlossen: 'animals.html' mit HTML-Tags generiert.")


if __name__ == "__main__":
    main()