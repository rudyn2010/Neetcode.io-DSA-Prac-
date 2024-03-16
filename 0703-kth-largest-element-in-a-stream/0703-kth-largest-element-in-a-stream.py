class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        # minHeap initially is an array when initialized, will turn into a heap using heapify, will give sorted property and run in O(n) time 
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Use heappush to add value to heap, regardless of what it is, big or to small
        heapq.heappush(self.minHeap, val)
        
        # Only want to pop from the heap when it is greater than k length elements, heap can be initialized with list less than k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)