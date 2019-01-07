from flask import Flask, jsonify
from flask_cors import CORS
from data.chords import chords

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/chord/<chord>')
def get_chord(chord):
    return jsonify(chords[chord])


if __name__ == '__main__':
    app.run()
