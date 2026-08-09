class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1

        for R in range(len(s1), len(s2)):
            if s1Freq == s2Freq:
                return True
            
            s2Freq[ord(s2[R]) - ord('a')] += 1
            
            s2Freq[ord(s2[R - len(s1)]) - ord('a')] -= 1

        return s1Freq == s2Freq
            
