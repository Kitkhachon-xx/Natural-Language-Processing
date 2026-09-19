import spacy
class SpacyProcess:
    def __init__(self, model_name='en_core_web_sm'):
        self.nlp = spacy.load(model_name)

    def process_text(self, text):
        doc = self.nlp(text)
        return doc

    def get_tokens(self, doc):
        text = [token.text for token in doc]
        pos = [token.pos_ for token in doc]
        dep = [token.dep_ for token in doc]
        head = [token.head.text for token in doc]
        return text, pos, dep, head