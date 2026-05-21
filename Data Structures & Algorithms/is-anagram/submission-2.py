class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap = dict()
        # for i in range(s):
        #     hashmap[i] = 0

        #     hashmap[i] += 1

        if sorted(s) == sorted(t):
            return True
        return False
            