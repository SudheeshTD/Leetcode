class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return [num for num, _ in Counter(nums).most_common(k)]
        
        '''
        d = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            d[i] = 1 + d.get(i,0)
        for n,c in d.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for fum in freq[i]:
                res.append(fum)
                if len(res) == k:
                    return res
        '''

'''
        freq = Counter(nums)
        arr_freq = freq.most_common()

        ar = []
        for i, _ in arr_freq:
            if k < 1:
                break
            k-=1
            ar.append(i)
        
        return ar
'''
        
        
        

            