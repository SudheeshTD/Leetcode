class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_two = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dict_two:
                dict_two[nums[i]] = i
            else:
                return [dict_two[diff],i]
                



        