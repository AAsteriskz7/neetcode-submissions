class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {};
        for i, num in enumerate(nums):
            complement = target - num;
            if complement in myDict:
                #found in dict
                complementIndex = myDict[complement];
                returnList = [complementIndex, i]
                #return i and complements index
                returnList.sort();
                break;
            else:
                myDict[num] = i;
        return returnList

#pseudocode
#loop through the list of nums
#as we loop through, we add the number's complement to the dictionary,
#if the complement is already in the dictionary, then we have found the match 
#and we can return the indeces of both numbers, smallest first
#else case, if the complement is not in the dictionary, then
#we need to add the number, index the dictionary. 
#and we repeat for rest of numbers until a match is found
#if match is found, we can break out of loop and return