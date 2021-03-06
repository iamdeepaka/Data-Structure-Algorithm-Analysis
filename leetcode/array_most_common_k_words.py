# Time: O(N log N)
# Space: O(N)

from collections import Counter

def mostCommonKWords(word_list, k):
    count = Counter(word_list)
    candidates = list(count.keys())
    candidates.sort(key=lambda w: (-count[w], w))
    return candidates[:k]


# Time: O(N log k)
# Space: O(N)

import heapq


def mostCommonKWords_Optimized(word_list, k):
    count = Counter(word_list)
    return heapq.nsmallest(k, count.keys(), key=lambda w: (-count(w), w))
