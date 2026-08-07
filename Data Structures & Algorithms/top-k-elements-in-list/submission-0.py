from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count Frequencies: O(n)
        # 'count' will be a dictionary like {number: frequency}
        count = Counter(nums) 
        
        # 2. Sort Based on Frequency: O(N log N) where N is the number of unique elements
        # We sort the items (key-value pairs) of the dictionary.
        # The key for sorting is the frequency (the second element, index 1)
        # reverse=True sorts from highest frequency to lowest.
        sorted_items = sorted(
            count.items(), 
            key=lambda item: item[1], 
            reverse=True
        )
        
        # 3. Extract Top K Elements: O(k)
        result = []
        for i in range(k):
            # item[0] is the number (the key in the dictionary)
            result.append(sorted_items[i][0])
            
        return result

# Example: nums = [1, 2, 2, 3, 3, 3], k = 2
# count = {1: 1, 2: 2, 3: 3}
# sorted_items = [(3, 3), (2, 2), (1, 1)] 
# result = [3, 2] (or [2, 3] since order doesn't matter)