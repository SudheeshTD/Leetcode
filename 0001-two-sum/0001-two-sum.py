# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_map = {}
#         n = len(nums)
#         for i in range(n):
#             comp = target - nums[i]

#             if comp in num_map:
#                 return [num_map[comp],i] 

#             num_map[nums[i]] = i
                

   
            

# To test Leethub v2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []