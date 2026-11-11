import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<username>", methods=["GET"])
def get_gists(username):
    url = f"https://api.github.com/users/{username}/gists"

    response = requests.get(url)
    gists = response.json()

    return jsonify(gists)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)