import numpy as np
import spacy
# from keras.preprocessing.text import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer

nlp = spacy.load('en',disable=['parser', 'tagger','ner'])


def tokenize_lemma(sentence):
    return [(token.lemma_).lower() for token in nlp(sentence)]


def bag_of_words(tokenized_sentence,all_words):
    bag=np.zeros(len(all_words),dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx]=1.0
    return bag


