import json


def load_data(file_path):
    """Loads animal data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes one animal into an HTML list item using safe access."""
    name = animal_obj.get('name')
    char = animal_obj.get('characteristics', {})
    locs = animal_obj.get('locations', [])

    output = '<li class="cards__item">\n'
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <div class="card__text">\n    <ul class="animal-details">\n'

    if char.get('diet'):
        output += f"      <li><strong>Diet:</strong> {char.get('diet')}</li>\n"
    if locs:
        output += f"      <li><strong>Location:</strong> {locs[0]}</li>\n"
    if char.get('type'):
        output += f"      <li><strong>Type:</strong> {char.get('type')}</li>\n"
    if char.get('skin_type'):
        output += f"      <li><strong>Skin Type:</strong> {char.get('skin_type')}</li>\n"

    output += '    </ul>\n  </div>\n</li>\n'
    return output


def main():
    """Main controller: Loads data, filters by skin type, and writes HTML."""
    data = load_data('animals_data.json')

    # Get skin types for the prompt
    skins = {a.get('characteristics', {}).get('skin_type') for a in data if
             a.get('characteristics', {}).get('skin_type')}
    print("Available Skin Types:", ", ".join(sorted(skins)))

    user_input = input("Enter a skin type to filter (or press Enter for all): ").strip()

    # Generate HTML content
    animals_html = ""
    for animal in data:
        if not user_input or animal.get('characteristics', {}).get('skin_type') == user_input:
            animals_html += serialize_animal(animal)

    # Replace and write file
    with open('animals_template.html', "r") as f:
        template = f.read()

    final_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as f:
        f.write(final_content)
    print("Successfully generated animals.html")


if __name__ == "__main__":
    main()