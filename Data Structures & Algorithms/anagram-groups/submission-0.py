class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnDict = {}
        for string in strs:
            #string is each string
            frequencyList = [0] * 26;
            for char in string:
                frequencyList[ord('a')-ord(char)] += 1;
            frequencyTuple = tuple(frequencyList);
            #if already in the dict
            if frequencyTuple in returnDict.keys():
                returnDict[frequencyTuple].append(string)
            #not in the dict
            else:
                returnDict[frequencyTuple] = [string]
        
        return list(returnDict.values())
        

#pseduocode
#loop through the input strs
#for each element in the list
#create an array of 26 spots
#ord('a')
#for the length of each element, add the character to an array
#act would be added in the a spot c spot and t spot

#repeat for the rest of the stuff
#hashmap with arrays as keys and values as the strings, (when we do the values we need to make the values lists)
#how do we return this it to the user
#get the values and thats the return output using myDict.values();, this returns a view object