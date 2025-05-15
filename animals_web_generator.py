import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)


output = ''
for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]

    output += '<li class="cards__item">'
    output += f"Name: {name}<br/>\n"
    output += f"Diet: {diet}<br/>\n"
    output += f"Location: {location}<br/>\n"

    if "type" in animal["characteristics"]:
        type = animal["characteristics"]["type"]
        output += f"Type: {type}<br/>\n"
    else:
        output += f"\n"

    output += '</li>'

print(output)

with open("animals_template.html", "r") as file:
    data = file.read()
    data = data.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals_template.html", "w") as file:
    file.write(data)
