import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')
print(animals_data)

for animal in animals_data:
    name_animal = animal['name']
    diet_animal = animal['characteristics']['diet']
    location_animal = animal['locations'][0]
    try:
        type_animal = animal['characteristics']['type']
        has_type = True
    except KeyError:
        has_type = False

    if has_type:
        print(f"Name: {name_animal}\n"
              f"Diet: {diet_animal}\n"
              f"Location: {location_animal}\n"
              f"Type: {type_animal}\n")
    else:
        print(f"Name: {name_animal}\n"
              f"Diet: {diet_animal}\n"
              f"Location: {location_animal}\n")