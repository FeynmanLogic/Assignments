import nltk
from nltk.util import ngrams

text = "This is Dhruv Kulkarni, trying to demonstrate what n-grams are. They work in funny ways."
words = nltk.word_tokenize(text)
def generate_ngrams(tokens, n):
    ngrams_list = ngrams(tokens, n)
    return [' '.join(gram) for gram in ngrams_list]
bi_grams = generate_ngrams(words, 2)
print("Bi-grams:")
print(bi_grams)
tri_grams = generate_ngrams(words, 3)
print("\nTri-grams:")
print(tri_grams)
