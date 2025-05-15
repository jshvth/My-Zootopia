import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)


for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]

    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"Location: {location}")

    if "type" in animal["characteristics"]:
        type = animal["characteristics"]["type"]
        print(f"Type: {type}")
    else:
        print()