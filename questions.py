import textchanges
import re

def words_from_words(question):
    question_text = re.sub(r'[^\w\s]', '', question)
    question_text = question_text.lower()
    words = question_text.split()
    words = list(filter(lambda x: x != '', words))
    return words

def find_common_terms(question, document):
    question_words = set(words_from_words(question))
    corpus_words = set(document.split())
    common_terms = question_words.intersection(corpus_words)
    return common_terms

def calculate_tf(question, corpus): #calculate the tf score of the question
    question_words = words_from_words(question)
    corpus_words = set(corpus.split())
    tf_scores = {}
    for word in question_words:
        if word in corpus_words:
            tf_scores[word] = question_words.count(word) / len(question_words)
        else:
            tf_scores[word] = 0
    return tf_scores


def calculate_tfidf(question, corpus_directory): #associate an idf score to the words of the question
    tf_scores = calculate_tf(question, corpus_directory)
    idf_scores = tf_idf(corpus_directory)
    tfidf_scores = {}
    for term in tf_scores:
        tfidf_scores[term] = tf_scores[term] * idf_scores[term]
    return tfidf_scores

def scalar_product(vectorA,vectorB): #returs the scalar product of the two vectors
    scalar = 0
    for i in range(len(vectorA)):
        scalar += vectorA[i]vectorB[i]
    return scalar

def norm(vector): #returns the norm of the vector
    norm = 0
    for i in range(len(vector)):
        norm += vector[i]2
    return norm(1/2)


def cosine_similarity(vectorA, vectorB): #returns the cosine similarity between the two vectors
    cosine = scalar_product(vectorA,vectorB)/(norm(vectorA)norm(vectorB))
    return cosine



