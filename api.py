from flask import Flask, request, jsonify
from reader import ReaderClass
from pprint import pprint
from webscraper import AnonymousScraper

app = Flask(__name__)

@app.route('/', methods=['POST'])

def UploadFile():
    if 'file' not in request.files:
        return jsonify({
            'error': 'Se requiere el archivo PDF'
        }), 400
    
    file = request.files['file']
    readerFile = ReaderClass(file)
    
    if not readerFile.isPdf():
        return jsonify({
            'error': 'Solo se acepta formato PDF'
        }), 400
        
    listUrls = readerFile.proccess()
    webScrap = AnonymousScraper()
    for i, url in enumerate(listUrls):
        text = webScrap.get_text(url) 
    webScrap.close()
    #pprint(listUrls, indent=2, width=100)
    return jsonify({
        'urls': listUrls,
        'text': text
    }), 200

if __name__ == '__main__':
    app.run(debug=True)