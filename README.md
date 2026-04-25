# Tweet Clustering (K-means)

## What this does

This program reads tweets from a file, cleans them, and groups them into clusters.

Each tweet is turned into a set of words, and we use Jaccard distance to measure how similar they are.

---

## Files

- main.py -> run everything here  
- preprocess.py -> clean tweets and convert to sets  
- jaccard.py -> compute distance  
- kmeans.py -> clustering part  

---

## How to run

Go to src folder first:

cd src  
python3 main.py  

If you run it somewhere else, it might not work because of the file path.

---

## Output

It will print:
- total number of tweets  
- SSE for each k  
- size of each cluster  

Example:
Value of K = 2  
SSE = 5306.4
Size of each cluster:  
1: 3421 tweets
2: 2819 tweets

---

## Libraries used

Just basic Python:
- re  
- random  

---

## Notes

- initial centroids are random  
- we set random.seed(123) so results don’t change every run  
- if a cluster is empty, it just picks a random tweet  

---

## Limitations

- only prints results (no file output)  
- a bit slow since it compares tweets in loops  
