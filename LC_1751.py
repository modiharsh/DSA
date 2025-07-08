# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii

from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        # Sort events by end day
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Precompute end days for binary search
        end_days = [event[1] for event in events]

        # Precompute prev array using binary search
        prev = [0] * n
        for i in range(n):
            prev[i] = bisect_right(end_days, events[i][0] - 1) 

        # Initialize DP table
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Skip current event
                dp[i][j] = dp[i - 1][j]
                # Take current event
                dp[i][j] = max(dp[i][j], dp[prev[i - 1]][j - 1] + events[i - 1][2])

        return dp[n][k]

# Example 1:
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

# Example 2:
# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# Output: 10
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.

# Example 3:
# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# Output: 9
# Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
