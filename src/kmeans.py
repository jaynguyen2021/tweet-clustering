# k-means clustering for tweet sets (using jaccard distance)

import random
from jaccard import jaccard_distance


def assign_clusters(tweets, centroids):
    # assign each tweet to the closest centroid
    clusters = [[] for _ in range(len(centroids))]

    for tweet in tweets:
        min_dist = float('inf')
        best_cluster = 0

        for i in range(len(centroids)):
            dist = jaccard_distance(tweet, centroids[i])

            if dist < min_dist:
                min_dist = dist
                best_cluster = i

        clusters[best_cluster].append(tweet)

    return clusters


def update_centroids(clusters, tweets):
    # update centroid by choosing a representative tweet
    new_centroids = []

    for cluster in clusters:
        # handle empty cluster
        if len(cluster) == 0:
            new_centroids.append(random.choice(tweets))
            continue

        best_tweet = None
        best_dist = float('inf')

        # try each tweet as centroid candidate
        for t1 in cluster:
            total_dist = 0

            for t2 in cluster:
                total_dist += jaccard_distance(t1, t2)

            avg_dist = total_dist / len(cluster)

            if avg_dist < best_dist:
                best_dist = avg_dist
                best_tweet = t1

        new_centroids.append(best_tweet)

    return new_centroids


def compute_sse(clusters, centroids):
    # compute sum of squared errors
    sse = 0

    for i in range(len(clusters)):
        cluster = clusters[i]

        for tweet in cluster:
            dist = jaccard_distance(tweet, centroids[i])
            sse += dist * dist

    return sse


def kmeans(tweets, k, max_iter=10):
    # pick initial centroids randomly
    centroids = random.sample(tweets, k)

    for _ in range(max_iter):
        clusters = assign_clusters(tweets, centroids)

        new_centroids = update_centroids(clusters, tweets)

        # stop if no change
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return clusters, centroids