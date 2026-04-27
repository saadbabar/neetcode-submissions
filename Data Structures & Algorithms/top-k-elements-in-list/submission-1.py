class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        # {1: 1 occurrence, 2: 2 occurrences,..}
        heap = []

        for val, freq in counter.items():
            # default min val will be at top min heap
            heapq.heappush(heap, (freq, val))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            freq, val = heapq.heappop(heap)
            res.append(val)

        return res


