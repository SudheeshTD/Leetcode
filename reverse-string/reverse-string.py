class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left: int, right: int) -> None:
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)
        
        helper(0, len(s) - 1)
            
            
            

        
        
        
        
        print()
        
        """
        Do not return anything, modify s in-place instead.
        """
        