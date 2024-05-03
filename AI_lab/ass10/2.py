import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import defaultdict

def generate_key_phrases(text, max_length=5):
    tokens = word_tokenize(text)
    key_phrases = defaultdict(list)
    for n in range(1, max_length + 1):
        n_grams = ngrams(tokens, n)
        for gram in n_grams:
            key_phrase = ' '.join(gram)
            key_phrases[n].append(key_phrase)
    
    return key_phrases

text = "Life is funny, in moments of happiness u cry and in moments of sadness u laugh it off."
key_phrases = generate_key_phrases(text)


for length, phrases in key_phrases.items():
    print(f"Key phrases of length {length}:")
    print(phrases)
    print()
