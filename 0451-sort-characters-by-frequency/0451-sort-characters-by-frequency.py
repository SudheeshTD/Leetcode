class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        freq = [[] for i in range(len(s)+1)]

        for i in s:
            d[i] = 1+ d.get(i,0)

        for n,c in d.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for char in freq[i]:
                res.append(char * i)

        return "".join(res)



        