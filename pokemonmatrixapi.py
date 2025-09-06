import requests
import json
url = "https://pokeapi.co/api/v2/type/"
response = requests.get(url).json()

types = [t["name"] for t in response["results"]]
types.sort()  
matrix = [[1 for _ in types] for _ in types]
for i, defender in enumerate(types):
    data = requests.get(f"https://pokeapi.co/api/v2/type/{defender}").json()
    relations = data["damage_relations"]

    for atk in relations["double_damage_from"]:
        j = types.index(atk["name"])
        matrix[i][j] = 2

    for atk in relations["half_damage_from"]:
        j = types.index(atk["name"])
        matrix[i][j] = 0.5

    for atk in relations["no_damage_from"]:
        j = types.index(atk["name"])
        matrix[i][j] = 0
print(" " * 12, end="")
for atk in types:
    print(f"{atk:<10}", end="")
print()
for i, defender in enumerate(types):
    print(f"{defender:<12}", end="") 
    for j, atk in enumerate(types):
        val = matrix[i][j]
        if val == 1:
            cell = " " 
        else:
            cell = str(val)
        print(f"{cell:<10}", end="")
    print()
output = {
    "types": types,
    "matrix": matrix
}
with open("type_matrix.json", "w") as f:
    json.dump(output, f, indent=4)
print("Saved in type_matrix.json")
