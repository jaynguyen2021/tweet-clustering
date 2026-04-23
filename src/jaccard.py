# jaccard distance between two tweets (sets of words)

def jaccard_distance(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)

    if union == 0:
        return 0

    return 1 - intersection / union