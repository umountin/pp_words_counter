from flask import Flask, jsonify, request, json

from text_analyzer import TextAnalyzer

app = Flask(__name__)

@app.route('/word_frequency_counter', methods = ['POST'])
def disp_word_frequency_counter():
    string = request.json['string']
    paragraph = TextAnalyzer(string)
    if isinstance(string, str) and paragraph.validate_paragraph_size():
        result = paragraph.word_frequency_counter()
        return jsonify(result)    
    elif isinstance(string, str) is False:
        return 'The paragraph should be only string.', 400    
    elif paragraph.validate_paragraph_size() is False:
        return 'The size of the paragraph is bigger than 500 words.', 413
    else:
        return 'I’m a teapot :)', 418

@app.route('/word_counter', methods = ['POST'])
def disp_word_counter():
    string = request.json['string']
    paragraph = TextAnalyzer(string)
    if isinstance(string, str) and paragraph.validate_paragraph_size():
        result = paragraph.word_counter()
        return jsonify(result)
    elif isinstance(string, str) is False:
        return 'The paragraph should be only string.', 400    
    elif paragraph.validate_paragraph_size() is False:
        return 'The size of the paragraph is bigger than 500 words.', 413
    else:
        return 'I’m a teapot :)', 418

@app.route('/char_counter', methods = ['POST'])
def disp_char_counter():
    string = request.json['string']
    paragraph = TextAnalyzer(string)
    if isinstance(string, str) and paragraph.validate_paragraph_size():
        result = paragraph.char_counter()
        return jsonify(result)
    elif isinstance(string, str) is False:
        return 'The paragraph should be only string.', 400    
    elif paragraph.validate_paragraph_size() is False:
        return 'The size of the paragraph is bigger than 500 words.', 413
    else:
        return 'I’m a teapot :)', 418   

@app.route('/flask_health_check', methods = ['GET'])
def flask_health_check():
    return 'success'