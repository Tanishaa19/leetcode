from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        return [num for num, count in freq.most_common(k)]