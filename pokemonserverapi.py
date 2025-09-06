import json
from flask import Flask, request

with open("type_matrix.json") as f:
    data = json.load(f)

types = data["types"]
matrix = data["matrix"]

app = Flask(__name__)

@app.route("/")
def home():
    atk = request.args.get("attacker")
    dfn = request.args.get("defender")

    result = {}

    if atk and dfn:
        i, j = types.index(atk), types.index(dfn)
        result = {"attacker": atk, "defender": dfn, "multiplier": matrix[i][j]}

    elif dfn:
        j = types.index(dfn)
        result = {dfn: dict(zip(types, matrix[j]))}

    elif atk:
        i = types.index(atk)
        col = {t: row[i] for t, row in zip(types, matrix)}
        result = {atk: col}

    else:
        result = {"error": "give attacker or defender"}

    # pretty print JSON vertically
    return app.response_class(
        response=json.dumps(result, indent=4),
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(port=8000)