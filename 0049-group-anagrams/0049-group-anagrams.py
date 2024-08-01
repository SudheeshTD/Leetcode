class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for i in strs:
            word = ''.join(sorted(i))
            d[word].append(i)

        return list(d.values())