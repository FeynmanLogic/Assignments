import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

text = """Machine Learning can usually be divided into 
                          classic Machine Learning and Deep Learning. 
                          Classic Machine Learning is relatively easy to understand. 
                          Deep Learning on the other hand is a bit more complex."""

sentences = sent_tokenize(text)

words = [word_tokenize(sentence) for sentence in sentences]

words_flat = [word for sentence in words for word in sentence]

pos_tags = pos_tag(words_flat)

def separate_into_phrases(text, n):
    words = text.split()
    phrases = []
    for i in range(0, len(words), n):
        phrase = " ".join(words[i:i+n])
        phrases.append(phrase)
    return phrases


n = 3 


phrases = separate_into_phrases(text, n)

total_sentences = len(sentences)

total_words = len(words_flat)


print("Total number of sentences:", total_sentences)
print("Total number of words:", total_words)
print("Parts of Speech tagging:", pos_tags)
print("Phrases of length", n, ":", phrases)
