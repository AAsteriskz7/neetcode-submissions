class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArr = [0] * len(nums);
        prefixArr = [0] * len(nums);
        postfixArr = [0] * len(nums);


        prefixArr[0] = postfixArr[len(nums) - 1] = 1
        #for loop is for the prefix array
        for i in range(1, len(nums)): #i is indicies
            prefixArr[i] = nums[i-1] * prefixArr[i-1]

        #for loop is for the postfix array
        for i in range(len(nums) -2, -1, -1):
            postfixArr[i] = nums[i+1] * postfixArr[i +1]
        
        #output
        for i in range(len(nums)):
            outputArr[i] = prefixArr[i] * postfixArr[i]
        
        return outputArr


        

#pseudocode
#starting array nums
#create our prefix array
#loop through the list, as we go we multiplty the prev number with curr number

#vice versa for postfix array (only thing that changes is we start from the back of the array)

#both arrays done
#for each element, multiply the prefix * suffix and put in new output array