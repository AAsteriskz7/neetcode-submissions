class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        midpoint = len(s)//2
        for i in range(midpoint):
            s[i], s[j] = s[j], s[i]
            j -= 1
            
        