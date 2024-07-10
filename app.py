from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# Load the trained NER model
nlp_custom = spacy.load(r"C:\Users\anany\OneDrive\Desktop\Output\model-best")

@app.route('/ner', methods=['POST'])
def get_product_entity():
    try:
        data = request.json
        text = data.get("text", "")
        if text:
            doc = nlp_custom(text)
            product_entities = [ent.text for ent in doc.ents if ent.label_ == "PRODUCT"]
            return jsonify({"product_entities": product_entities})
        else:
            return jsonify({"error": "Text not provided"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
