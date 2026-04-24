# main file to run tweet clustering

from preprocess import load_tweets
from kmeans import kmeans, compute_sse
import random
random.seed(123)

tweets = load_tweets("../data/nytimeshealth.txt")

print("total tweets: ", len(tweets))

# values of k to test
k_values = [2, 3, 7, 10, 14]

print("\n******** results table ********")

for k in k_values:
    clusters, centroids = kmeans(tweets, k)
    sse = compute_sse(clusters, centroids)

    print("\nValue of K =", k)
    print("SSE =", round(sse, 4))

    print("Size of each cluster:")
    for i, cluster in enumerate(clusters):
        print(f"{i+1}: {len(cluster)} tweets")