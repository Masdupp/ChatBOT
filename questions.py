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

def calculate_tf(question, document): #calculate the tf score of the question
    question_words = words_from_words(question)
    corpus_words = set(document.split())
    tf_scores = {}
    for word in question_words:
        if word in corpus_words:
            tf_scores[word] = question_words.count(word) / len(question_words)
        else:
            tf_scores[word] = 0
    return tf_scores


def calculate_tfidf(question, document_directory): #associate an idf score to the words of the question
    tf_scores = calculate_tf(question, document_directory)
    idf_scores = tf_idf(document_directory)
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


def find_most_relevant(tfidf_matrix, tfidf_vector, file_names): #find the most relevant document in the cleaned directory
    similarities = cosine_similarity(tfidf_matrix, tfidf_vector)
    most_relevant_index = similarities.argmax()
    return file_names[most_relevant_index]

def get_speeches_file_name(cleaned_file_name): #get the equivalent document from cleaned into speeches
    return cleaned_file_name.replace("./cleaned", "./speeches")

def find_keyword_and_sentence(tfidf_vector, tfidf_feature_names, document): #Locate the word with the highest TF-IDF score and locate the first occurence of the word in the relevant document, and then return the sentence containing the keyword as answer
    keyword_index = tfidf_vector.argmax()
    keyword = tfidf_feature_names[keyword_index]

    sentences = document.split('". "')
    for sentence in sentences:
        if keyword in sentence:
            return keyword, '"' + sentence + '"'

    return None, None