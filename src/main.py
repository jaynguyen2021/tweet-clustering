# main file to run tweet clustering

from preprocess import load_tweets
from kmeans import kmeans, compute_sse
import random
random.seed(123)

tweets = load_tweets("../data/nytimeshealth.txt")

print("total tweets: ", len(tweets))

# values of k to test
k_values = [2, 3, 5, 8, 10]

print("\n******** results ********")

for k in k_values:
    clusters, centroids = kmeans(tweets, k)
    sse = compute_sse(clusters, centroids)

    print(f"k = {k}, SSE = {round(sse, 4)}")
