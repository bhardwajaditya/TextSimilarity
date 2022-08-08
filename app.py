import os
from flask import Flask, jsonify, request,make_response
from dotenv import load_dotenv

from nlp import getSimilarQuestion

app = Flask(__name__)
load_dotenv()

@app.route('/api/similarity', methods=['POST'])
def similarity():
    if request.method == 'POST':
        data = request.get_json()
        result = getSimilarQuestion(data['questions'], data['target'])
        return make_response(jsonify(result), 200)
    return make_response(jsonify({'error': 'Invalid request'}), 400)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port='8080' ,debug=True)