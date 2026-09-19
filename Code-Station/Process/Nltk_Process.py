import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, ne_chunk
from nltk.corpus import stopwords

class NltkProcessor:
    def tokenize(self, text):
        return word_tokenize(text)

    def sent_tokenize(self, text):
        return sent_tokenize(text)

    def pos_tag(self, tokens):
        return pos_tag(tokens)

    def ne_chunk(self, tokens):
        return ne_chunk(tokens)

    def get_stopwords(self):
        return set(stopwords.words('english'))