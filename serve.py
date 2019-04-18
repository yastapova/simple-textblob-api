import textblob as tb

# tag input text with part-of-speech tags
def tag_pos(text):
    blob = tb.TextBlob(text)
    pos = blob.tags

    return pos

# calculate sentiment polarity score of input text [-1, 1]
def calc_sentiment_score(text):
    blob = tb.TextBlob(text)
    sent = blob.sentiment.polarity

    return sent

# autocorrect any spelling mistakes in input text
def autocorrect_text(text):
    blob = tb.TextBlob(text)
    new_text = blob.correct()

    return new_text.raw

# translate input text to the given language
def translate_text(text, to_lang):
    blob = tb.TextBlob(text)
    translated = blob.translate(to=to_lang)

    return translated.raw