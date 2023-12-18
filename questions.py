import textchanges
import re

def words_from_words(question):
    question_text = re.sub(r'[^\w\s]', '', question_text)
    question_text = question_text.lower()
    words = question_text.split()
    words = list(filter(lambda x: x != '', words))
    return words

def find_common_terms(question, document):
    question_words = set(words_from_words(question))
    corpus_words = set(document.split())
    common_terms = question_words.intersection(corpus_words)
    return common_terms

