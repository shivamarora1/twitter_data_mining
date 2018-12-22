# Identifies the tokens in the tweets

import json
import re
import string

from nltk.corpus import stopwords
from collections import Counter

# Getting the punctuations marks(.?/#$,)
punctuations = list(string.punctuation)
stop_words = stopwords.words('english') + punctuations + ['rt','RT','via','VIA','Rt','.','?']

# String of all the emotions
emotion_str = r"""
    (?:
        [:=;][oO\-]?[D\)\]\(\]/\\OpP]
    )"""

# String regex to find html tags,@ mentions,# hashtags,urls,numbers,charaters and words
regex_str =[
            emotion_str,
            r'<[^>]+>',
            r'(?:@[\w_]+)',
            r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
            r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
            r'(?:(?:\d+,?)+(?:\.?\d+)?)',
            r"(?:[a-z][a-z'\-_]+[a-z])",
            r'(?:[\w_]+)',
            r'(?:\S)'
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')',re.VERBOSE | re.IGNORECASE)
emotion_re = re.compile(r'^'+emotion_str+'$',re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

 # Function to convert tweet into the tokens
def preprocess(s,lowercase = True):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emotion_re.search(token) else token.lower() for token in tokens]
    return tokens


 # Function to count the frequency of the words in tweet
def count_frequency(file_name):
    word_counter = Counter()
    hashtags_counter = Counter()
    mentions_counter = Counter()

    with open(file_name,'r') as f:
        for line in f:
            if line is not '\n':
                tweet_obj = json.loads(line)
                tweet = tweet_obj['text']
                word_frequency = [tokens for tokens in preprocess(tweet)
                                    if tokens not in stop_words and not tokens.startswith(('#','@'))]
                hashtags_frequency = [tokens for tokens in preprocess(tweet)
                                        if tokens not in stop_words and tokens.startswith('#')]
                mentions_frequency = [tokens for tokens in preprocess(tweet)
                                        if tokens not in stop_words and tokens.startswith('@')]

                word_counter.update(word_frequency)
                hashtags_counter.update(hashtags_frequency)
                mentions_counter.update(mentions_frequency)
    
    return word_counter.most_common(20),hashtags_counter.most_common(20),mentions_counter.most_common(20)
