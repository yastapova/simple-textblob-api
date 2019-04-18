import json
from flask import Flask, request
import serve

app = Flask(__name__)

# dummy ping page
@app.route('/', methods=['GET'])
@app.route('/ping', methods=['GET'])
def index():
    return "Simple TextBlob API is running."

# tag input text with part-of-speech tags
@app.route('/TagPOS', methods=['POST'])
def tag_pos():
    text = request.json
    pos = serve.tag_pos(text)
    response = json.dumps(pos)

    return response

# calculate sentiment polarity score of input text [-1, 1]
@app.route('/CalcSentimentScore', methods=['POST'])
def calc_sentiment_score():
    text = request.json
    sent = serve.calc_sentiment_score(text)
    response = json.dumps(sent)

    return response

# autocorrect any spelling mistakes in input text
@app.route('/AutocorrectText', methods=['POST'])
def autocorrect_text():
    text = request.json
    new_text = serve.autocorrect_text(text)
    response = json.dumps(new_text)

    return response

# translate input text to the given language
@app.route('/TranslateText/<to_lang>', methods=['POST'])
def translate_text(to_lang):
    text = request.json
    translated = serve.translate_text(text, to_lang)
    response = json.dumps(translated)

    return response