class Solution:

    def encode(self, strs: List[str]) -> str:
        # eString = "";
        # for string in strs:
        #     strLen = len(string)
        #     eString += str(strLen)
        #     eString += '~'
        #     eString += string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    #encoded string example: 2#stringlength ...
    #steps
    #loop through the strings in the input
    #for each string in strings
    #calculate the length of the string
    #concat it to the leng, delim, string itself

    def decode(self, s: str) -> List[str]:
        # for i in range(len(s)):
        #     tempStr = ""
        #     returnList = []
        #     indexofD = 0
        #     tempStr += s[i]
        #     if s[i] = '~':
        #         indexofD = i
        #         length = int(tempStr)
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
                


            

    #encoded string exmaple: 2#strlen...
    #steps
    #start a loop from the beginning of the string
    #keep going until i find the ~
    #once i find ~, get the number before the delimeter (this will be all the accumulated characters until the delimeter)