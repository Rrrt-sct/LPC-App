# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import epitran
import os

app = Flask(__name__)
CORS(app)  # Permet les appels JS en local (CORS)

# Initialise Epitran pour le français
epi = epitran.Epitran('fra-Latn')

@app.route('/transcrire', methods=['POST'])
def transcrire():
    data = request.get_json()
    texte = data.get('texte', '')
    ipa = epi.transliterate(texte)
    return jsonify({'phonemes': ipa})

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    # Assure-toi que l'encodage est correct (utile si variable PYTHONUTF8 non définie)
    os.environ["PYTHONIOENCODING"] = "utf-8"
    app.run(debug=True)