class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dict = {} #hashmap
        # for i in range(len(nums)):
        #     if nums[i] in dict:
        #         dict[nums[i]] += 1
        #         return True
        #     else:
        #         dict[nums[i]] = 0
        # return False

        hashset =  set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False