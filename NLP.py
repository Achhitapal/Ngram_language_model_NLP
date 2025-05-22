import nltk
from nltk.util import ngrams
from collections import Counter, defaultdict
import random

# Dataset: Paste your sentences here
sentences = [
    "how are you doing today",
    "i am doing fine",
    "what are you doing",
    "are you coming today",
    "yes i am coming",
    "no i am busy",
    "how is your day",
    "my day is good",
    "do you want to eat",
    "i want pizza",
    "do you have money",
    "yes i have some",
    "let's go to the cafe",
    "we can meet there",
    "okay see you at five",
    "thank you so much",
    "you're welcome",
    "i will call you later",
    "please bring your notebook",
    "i don't have a pen",
    "where are we going",
    "let's meet at the park",
    "do you like ice cream",
    "i love chocolate flavor",
    "can we go now",
    "i need to study",
    "my exam is tomorrow",
    "he is a good friend",
    "she is my best friend",
    "we had so much fun",
    "what is your favorite movie",
    "i like action movies",
    "the weather is very nice",
    "it is going to rain",
    "don't forget your umbrella",
    "we are planning a trip",
    "where do you want to go",
    "i want to go to the beach",
    "let's watch a movie tonight",
    "what time will you come",
    "i will be there at eight",
    "we can order food online",
    "he is not picking up the phone",
    "she called me in the morning",
    "i was sleeping then",
    "are you free tomorrow",
    "let's study together",
    "i am feeling tired",
    "you should take some rest",
    "drink water and relax"
]

# Tokenize sentences
tokens = [sentence.lower().split() for sentence in sentences]
unigrams = []
bigrams = []
trigrams = []

for sentence in tokens:
    unigrams += sentence
    bigrams += list(ngrams(sentence, 2))
    trigrams += list(ngrams(sentence, 3))

# Frequency counts
unigram_freq = Counter(unigrams)
bigram_freq = Counter(bigrams)
trigram_freq = Counter(trigrams)

# 🔮 Next-word prediction using bigram/trigram
def predict_next_word(context, n=3):
    context = tuple(context.lower().split())
    if len(context) == 1:
        candidates = {k[1]: v for k, v in bigram_freq.items() if k[0] == context[0]}
    elif len(context) == 2:
        candidates = {k[2]: v for k, v in trigram_freq.items() if k[0] == context[0] and k[1] == context[1]}
    else:
        return "Context too long. Use 1 or 2 words only."

    if not candidates:
        return "No suggestion"

    sorted_candidates = sorted(candidates.items(), key=lambda item: item[1], reverse=True)
    return [word for word, _ in sorted_candidates[:n]]

# 🛠 Basic Autocorrect Simulation using Trigram Context
def autocorrect_trigram(context):
    w1, w2 = context.lower().split()
    possibilities = [k[2] for k in trigram_freq if k[0] == w1 and k[1] == w2]
    return max(possibilities, key=lambda word: trigram_freq[(w1, w2, word)], default="No suggestion")

# 🧪 Example Usage
print("Unigram Frequency (top 5):", unigram_freq.most_common(5))
print("Next word after 'i am':", predict_next_word("i am"))
print("Next word after 'let's':", predict_next_word("let's"))
print("Autocorrect (context = 'i am'):", autocorrect_trigram("i am"))
