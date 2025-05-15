import json


def load_data(file_path):
    """
    Loads and returns JSON data from a file.

    :param file_path: Path to the JSON file.
    :return: Parsed JSON data.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def generate_html(animals_data):
    """
    Generates HTML string for a list of animals.

    :param animals_data: List of dictionaries with animal data.
    :return: HTML string with formatted animal info.
    """
    output = ""

    for animal in animals_data:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = animal["locations"][0]

        output += '<li class="cards__item">'
        output += f'<div class="card__title">{name}</div>'
        output += '<p class="card__text">\n'
        output += f'<strong>Diet:</strong> {diet}<br/>\n'
        output += f'<strong>Location:</strong> {location}<br/>\n'

        if "type" in animal["characteristics"]:
            type = animal["characteristics"]["type"]
            output += f'<strong>Type:</strong> {type}<br/>\n'
        else:
            output += '<br/>\n'

        output += '</p>\n'
        output += '</li>'

    return output


def inject_html(template_path, output_html, placeholder="__REPLACE_ANIMALS_INFO__"):
    """
    Replaces a placeholder in an HTML file with generated HTML content.

    :param template_path: Path to the HTML template file.
    :param output_html: HTML string to inject.
    :param placeholder: Placeholder string to be replaced.
    """
    with open(template_path, "r", encoding="utf-8") as file:
        data = file.read()
        data = data.replace(placeholder, output_html)

    with open(template_path, "w", encoding="utf-8") as file:
        file.write(data)


def main():
    animals_data = load_data("animals_data.json")
    output_html = generate_html(animals_data)
    inject_html("animals_template.html", output_html)


if __name__ == "__main__":
    main()
