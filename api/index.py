from flask import Flask, jsonify, request, render_template
import requests
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)

# Enable CORS for all routes, allowing requests from any origin
CORS(app)  


# Firebase Realtime Database URL and Path
DATABASE_URL = "https://darija2024-database-default-rtdb.firebaseio.com/"
PATH = "darija-words.json"

def fetch_data():
    """Fetch data from Firebase Realtime Database."""
    url = f"{DATABASE_URL}/{PATH}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def home():
    return render_template('main.html')  # Render the HTML template

@app.route('/words', methods=['GET'])
def get_all_words():
    """Get all words."""
    data = fetch_data()
    if data:
        return jsonify({"data": data})
    else:
        return jsonify({"error": "Unable to fetch data"}), 500

@app.route('/words/<string:word_type>', methods=['GET'])
def get_words_by_type(word_type):
    """Get words by type (e.g., noun, verb, adj, adv, pronoun)."""
    data = fetch_data()
    if data:
        filtered_words = {k: v for k, v in data.items() if v.get("type") == word_type}
        return jsonify({"data": filtered_words})
    else:
        return jsonify({"error": "Unable to fetch data"}), 500

@app.route('/words/<string:word_id>', methods=['GET'])
def get_word_by_id(word_id):
    """Get a specific word by its ID."""
    data = fetch_data()
    if data:
        word = data.get(word_id)
        if word:
            return jsonify({"data": word})
        else:
            return jsonify({"error": "Word not found"}), 404
    else:
        return jsonify({"error": "Unable to fetch data"}), 500

@app.route('/search', methods=['GET'])
def search_words():
    """Search for words by query (translation or word)."""
    query = request.args.get('q')
    word_type = request.args.get('type')
    data = fetch_data()
    if data:
        results = {}
        for word_id, word_data in data.items():
            if (query.lower() in word_data.get("translation", "").lower() or
                query.lower() in word_data.get("word", "").lower()):
                if not word_type or word_data.get("type") == word_type:
                    results[word_id] = word_data
        return jsonify({"data": results})
    else:
        return jsonify({"error": "Unable to fetch data"}), 500

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
