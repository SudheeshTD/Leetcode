class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)

        for x in s:
            dic[x] += 1
        for x in t:
            dic[x] -= 1
        for val in dic.values():
            if val!=0:
                return False
        return True
        