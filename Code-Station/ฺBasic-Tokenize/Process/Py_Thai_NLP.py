from pythainlp.tokenize import word_tokenize as th_word_tokenize
from pythainlp.tag import pos_tag as th_pos_tag
from pythainlp.corpus import thai_stopwords

class PyThaiNLPProcessor:
    def tokenize(self, text):
        return th_word_tokenize(text)
    
    def get_stopwords(self):
        return thai_stopwords()

    def pos_tag(self, tokens):
        return th_pos_tag(tokens)
    def tokenize_engine(self, text, engine=["newmm", "longest", "mm"]):
        results = {}
        for eng in engine:
            try:
                tokens = th_word_tokenize(text, engine=eng)
                print(f"{eng:>10}: {tokens}")
                results[eng] = tokens
            except Exception as e:
                print(f"Error with engine {eng}: {e}")
        return results