# Tweet Clustering with Jaccard Distance

This repository contains a Python implementation of tweet clustering for an ML assignment. The code loads tweets from the provided dataset, preprocesses each tweet into a set of tokens, clusters the tweets using a k-means style procedure with Jaccard distance, and reports the sum of squared errors (SSE) and cluster sizes for multiple values of `k`.

## Assignment Summary

The project is organized around the standard tweet-clustering workflow required by the assignment:

- read tweet records from the input file
- clean and tokenize tweet text
- represent each tweet as a set of words
- cluster tweets using Jaccard distance
- evaluate the clustering with SSE
- report results for several cluster counts

In this implementation, the program evaluates:

- `k = 2`
- `k = 3`
- `k = 7`
- `k = 10`
- `k = 14`

## Project Structure

```text
tweet-clustering/
├── data/
│   └── nytimeshealth.txt
├── src/
│   ├── main.py
│   ├── preprocess.py
│   ├── jaccard.py
│   └── kmeans.py
├── requirements.txt
└── README.md
```

## How the Code Works

### 1. Preprocessing

`src/preprocess.py` performs tweet cleaning before clustering.

The preprocessing step:

- removes URLs
- removes `@mentions`
- removes the `#` symbol but keeps the hashtag word
- converts text to lowercase
- removes punctuation and non-alphanumeric characters
- collapses extra whitespace
- converts each cleaned tweet into a set of words

Each tweet is therefore represented as a set, which is required for Jaccard distance.

### 2. Jaccard Distance

`src/jaccard.py` defines the distance between two tweets:

```text
Jaccard distance = 1 - (intersection / union)
```

This is suitable for short text documents represented as sets of tokens.

### 3. Clustering

`src/kmeans.py` implements the clustering logic.

The algorithm used here works as follows:

1. Randomly choose `k` tweets as initial centroids.
2. Assign each tweet to the nearest centroid using Jaccard distance.
3. Update each centroid by selecting the tweet in the cluster with the minimum average distance to the other tweets in that cluster.
4. Repeat until the centroids stop changing or `max_iter=10` is reached.

This is a practical k-means style approach for set-based tweet data, where the centroid is chosen from actual tweets instead of computing a numeric mean.

### 4. Evaluation

`src/main.py` computes and prints:

- total number of processed tweets
- SSE for each value of `k`
- size of each cluster

The SSE is computed as the sum of squared Jaccard distances between each tweet and its assigned centroid.

## Input Data Format

The dataset file used by the code is:

```text
data/nytimeshealth.txt
```

Each line is expected to follow this format:

```text
tweet_id|timestamp|tweet_text
```

The loader ignores malformed lines and skips tweets that become empty after preprocessing.

## Requirements

This project uses Python 3 and only standard-library modules in the current implementation. The `requirements.txt` file is present for project completeness, but the source code itself does not depend on external packages.

## How to Run

Because `src/main.py` reads the dataset using a relative path of `../data/nytimeshealth.txt`, run the program from the `src` directory:

```bash
cd src
python3 main.py
```

If you run `python3 src/main.py` from the repository root, the current path handling will fail because the script expects the working directory to be `src/`.

## Expected Output

The program prints a results table similar to:

```text
total tweets: <number>

******** results table ********

Value of K = 2
SSE = ...
Size of each cluster:
1: ... tweets
2: ... tweets
```

The same format is repeated for each tested value of `k`.

## Notes on Reproducibility

- `random.seed(123)` is set in `main.py`
- initial centroids are chosen randomly
- empty clusters are handled by reassigning a random tweet as the new centroid

This makes the clustering behavior more stable across runs.

## Files to Review

If this repository is being submitted for the assignment, the main files to review are:

- `src/main.py`
- `src/preprocess.py`
- `src/jaccard.py`
- `src/kmeans.py`

## Limitations

- the current implementation prints results to the console only
- cluster contents and centroid tweet IDs are not written to an output file
- the entry-point script depends on the current working directory
- runtime can be high for larger datasets because centroid updates compare tweets pairwise within each cluster
