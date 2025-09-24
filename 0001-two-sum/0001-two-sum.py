class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]

            if comp in num_map:
                return [num_map[comp],i] 

            num_map[nums[i]] = i
                

   
            