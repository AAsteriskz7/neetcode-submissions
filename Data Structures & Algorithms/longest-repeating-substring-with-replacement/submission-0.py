class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        max_freq = 0
        longest = 0
        L = 0

        for R in range(len(s)):
            charMap[s[R]] = charMap.get(s[R], 0) + 1
            max_freq = max(max_freq, charMap[s[R]])

            # Shrink window if replacements needed exceed k
            while (R - L + 1) - max_freq > k:
                charMap[s[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)

        return longest