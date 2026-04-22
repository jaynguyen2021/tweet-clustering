# preprocess tweets for clustering
import re


def clean_tweet(text):
    # basic cleaning for tweets
    text = re.sub(r'http\S+', '', text)        # remove urls
    text = re.sub(r'@\w+', '', text)           # remove mentions
    text = re.sub(r'#(\w+)', r'\1', text)      # remove # but keep word
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)    # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()   # clean extra spaces

    return text


def tweet_to_set(text):
    words = text.split()
    return set(w for w in words if w)          # remove empty words


def load_tweets(file_path):
    tweet_sets = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('|')

            if len(parts) < 3:
                continue

            raw_text = parts[-1]

            cleaned = clean_tweet(raw_text)
            word_set = tweet_to_set(cleaned)

            if word_set:                      # skip empty tweets
                tweet_sets.append(word_set)

    return tweet_sets