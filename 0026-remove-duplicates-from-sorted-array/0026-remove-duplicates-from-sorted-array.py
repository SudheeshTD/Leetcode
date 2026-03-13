class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'i' is the index of the last unique element found
        i = 0
        
        # 'j' scans the array starting from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements is i + 1
        return i + 1