# modules/labeling.py
import spacy

nlp = spacy.load("en_core_web_sm")

def label_token(token):
    tag_map = {
        "DET": "D",
        "NOUN": "N",
        "PROPN": "N",
        "VERB": "V",
        "AUX": "T",
        "ADJ": "Adj",
        "ADV": "Adv",
        "ADP": "P",
        "PRON": "N",
        "CONJ": "CONJ",
        "CCONJ": "CONJ",
        "PUNCT": "PUNCT",
    }
    return tag_map.get(token.pos_, "UNK")

def label_sentence(sentence):
    doc = nlp(sentence)
    labeled = [(label_token(tok), tok.text) for tok in doc]
    print("✅ POS tagging result:")
    for tok in doc:
        print(f"  {tok.text} → POS: {tok.pos_}, label: {label_token(tok)}")
    return labeled
