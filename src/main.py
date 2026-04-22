from preprocess import load_tweets

tweets = load_tweets("../data/nytimeshealth.txt")

print("total tweets: ", len(tweets))

for i in range(3):
    print(tweets[i])

for i in range(5):
    print("tweet", i, "size ", len(tweets[i]))
