import requests
import json
import sys
if len(sys.argv) > 1:
    output_file = sys.argv[1]
else:
    output_file = "pokemons.json"
pokemons = {}
file = open("pokemons.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    name = line.strip()
    if name == "":
        continue
    url_pokemon = "https://pokeapi.co/api/v2/pokemon/" + name.lower()
    url_species = "https://pokeapi.co/api/v2/pokemon-species/" + name.lower()
    pokemon_data = requests.get(url_pokemon).json()
    species_data = requests.get(url_species).json()
    poke_id = pokemon_data["id"]
    abilities = []
    for ab in pokemon_data["abilities"]:
        abilities.append(ab["ability"]["name"])
    types = []
    for t in pokemon_data["types"]:
        types.append(t["type"]["name"])
    is_legendary = species_data["is_legendary"]
    is_mythical = species_data["is_mythical"]
    pokemons[name] = {
        "id": poke_id,
        "abilities": abilities,
        "type": types,
        "is_legendary": is_legendary,
        "is_mythical": is_mythical
    }
f = open(output_file, "w")
json.dump(pokemons, f, indent=4)
f.close()

print("Saved in", output_file)
