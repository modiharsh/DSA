# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort()

        min_heap = []
        attended = 0
        i = 0
        day = 1
        n = len(events)

        while i < n or min_heap:
            # Push the possible events' end date to the heap
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Remove the expired events which were not picked
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
                day += 1
            elif i<n:
                # No other possible events to pick
                day = events[i][0]

        return attended

# Example 1:

# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# Example 2:

# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
