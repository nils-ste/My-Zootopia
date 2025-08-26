import json

with open ('animals_template.html', 'r') as template:
    animals_template = template.read()


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''
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
        # append information to each string
        output += '<li class="cards__item">'
        output += (f"Name: {name_animal}<br/>\n"
              f"Diet: {diet_animal}<br/>\n"
              f"Location: {location_animal}<br/>\n"
              f"Type: {type_animal}<br/>\n\n")
        output += '</li>'
    else:
        output += '<li class="cards__item">'
        output += (f"Name: {name_animal}<br/>\n"
              f"Diet: {diet_animal}<br/>\n"
              f"Location: {location_animal}<br/>\n\n")
        output += '</li>'

animals_output = animals_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open ('animals.html', 'w') as out:
    out.write(animals_output)