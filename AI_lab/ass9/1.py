from nltk.tokenize import word_tokenize
import nltk
import ssl


# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
text = " I am Dhruv Kulkarni, I am from Pune, This college is SVNIT. This is warm and humid climate. "


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
freq_dist = FreqDist(lemmatized_tokens)
print(freq_dist.most_common())
print("Stemmed tokens:", stemmed_tokens)
print("Lemmatized tokens:", lemmatized_tokens)



