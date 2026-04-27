class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1
        
        pq = []
        for val, freq in my_dict.items():
            heapq.heappush(pq, (freq, val))
            if (len(pq) > k):
                heapq.heappop(pq)
        
        sol = []
        while pq:
            freq, val = heapq.heappop(pq)
            sol.append(val)
        return sol

