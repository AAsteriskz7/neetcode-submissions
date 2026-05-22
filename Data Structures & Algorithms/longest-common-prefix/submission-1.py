class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])): #iterate through the length of first string. 
            for string in strs: #check each string
                if i == len(string) or string[i] != strs[0][i]: #first case checks lenght. second base checks each string with first string index
                    return string[:i] #returns everything before the current index
        return strs[0] #return first thing if we finish whole loop and dont find. 