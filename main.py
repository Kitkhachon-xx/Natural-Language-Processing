from Util.load_utils import load_config
from Process.Nltk_Process import NltkProcessor
from Process.Spacy_Process import SpacyProcess
from Process.Py_Thai_NLP import PyThaiNLPProcessor

def main():
    config = load_config('config.yaml')
    nltk_processor = NltkProcessor()
    spacy_processor = SpacyProcess()
    thai_processor = PyThaiNLPProcessor()
    text = config.get('text', '')
    th_text = config.get('th_text', '')
    tokens = nltk_processor.tokenize(text)
    sentences = nltk_processor.sent_tokenize(text)
    pos_tags = nltk_processor.pos_tag(tokens)
    named_entities = nltk_processor.ne_chunk(pos_tags)
    print("Sentences:", sentences)
    print("POS Tags:", pos_tags)
    print("Named Entities:", named_entities)
    cleaned_tokens = [token for token in tokens if token.lower() not in nltk_processor.get_stopwords()]
    print("Tokens:", tokens)
    print("Cleaned Tokens:", cleaned_tokens)

    print("\nSpacy Processing:")
    spacy_doc = spacy_processor.process_text(text)
    spacy_tokens, spacy_pos, spacy_dep, spacy_head = spacy_processor.get_tokens(spacy_doc)
    print("Spacy Tokens:", spacy_tokens)
    print("Spacy POS:", spacy_pos)
    print("Spacy Dependency:", spacy_dep)
    print("Spacy Head:", spacy_head)

    print("\nThai NLP Processing:")
    th_tokens = thai_processor.tokenize(th_text)
    cleaned_th_tokens = [token for token in th_tokens if token not in thai_processor.get_stopwords()]
    th_pos_tags = thai_processor.pos_tag(th_tokens)
    print("Thai Tokens:", th_tokens)
    print("Cleaned Thai Tokens:", cleaned_th_tokens)
    print("Thai POS Tags:", th_pos_tags)
    thai_processor.tokenize_engine(th_text, engine=["newmm", "longest", "mm"])
if __name__ == "__main__":
    main()