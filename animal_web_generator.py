import json


def load_data(file_path):
    """Loads animal data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(template_path):
    """Reads the HTML template file."""
    with open(template_path, "r") as f:
        return f.read()


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML card using safe access."""
    name = animal_obj.get('name')
    characteristics = animal_obj.get('characteristics', {})
    locations = animal_obj.get('locations', [])

    output = '<li class="cards__item">\n'
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    diet = characteristics.get('diet')
    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    animal_type = characteristics.get('type')
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n</li>\n'
    return output


def write_html_file(file_path, content):
    """Writes the final HTML content to a file."""
    with open(file_path, "w") as f:
        f.write(content)


def main():
    """
    Orchestrates the conversion of JSON animal data into a formatted
    HTML website using a predefined template.
    """
    animals_data = load_data('animal_data.json')
    template_content = read_template('animal_template.html')

    animals_html = ''.join([serialize_animal(animal) for animal in animals_data])

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    write_html_file("animals.html", final_html)
    print("Website generated.")


if __name__ == "__main__":
    main()