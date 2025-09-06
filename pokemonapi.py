import requests
import json
import sys

# check if output filename is given
if len(sys.argv) > 1:
    output_file = sys.argv[1]
else:
    output_file = "pokemons.json"

# dictionary to store all pokemons
pokemons = {}

# open the text file and read all names
file = open("pokemons.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    name = line.strip()
    if name == "":
        continue

    # urls
    url_pokemon = "https://pokeapi.co/api/v2/pokemon/" + name.lower()
    url_species = "https://pokeapi.co/api/v2/pokemon-species/" + name.lower()

    # get data from api
    pokemon_data = requests.get(url_pokemon).json()
    species_data = requests.get(url_species).json()

    # take id
    poke_id = pokemon_data["id"]

    # take abilities
    abilities = []
    for ab in pokemon_data["abilities"]:
        abilities.append(ab["ability"]["name"])

    # take types
    types = []
    for t in pokemon_data["types"]:
        types.append(t["type"]["name"])

    # take legendary and mythical
    is_legendary = species_data["is_legendary"]
    is_mythical = species_data["is_mythical"]

    # put in dictionary
    pokemons[name] = {
        "id": poke_id,
        "abilities": abilities,
        "type": types,
        "is_legendary": is_legendary,
        "is_mythical": is_mythical
    }

# save in json file
f = open(output_file, "w")
json.dump(pokemons, f, indent=4)
f.close()

print("Saved in", output_file)
