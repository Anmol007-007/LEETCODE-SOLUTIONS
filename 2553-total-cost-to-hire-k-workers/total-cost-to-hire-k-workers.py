class Solution:
  def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
    n = len(costs)
    left_ptr = candidates
    right_ptr = n - candidates

    if left_ptr >= right_ptr:
      heapq.heapify(costs)
      total = 0
      for _ in range(k):
        total += heapq.heappop(costs)
      return total

    left_heap = costs[:candidates]
    right_heap = costs[right_ptr:]

    heapq.heapify(left_heap)
    heapq.heapify(right_heap)

    total_cost = 0

    for _ in range(k):
      if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
        total_cost += heapq.heappop(left_heap)
        if left_ptr < right_ptr:
          heapq.heappush(left_heap, costs[left_ptr])
          left_ptr += 1
      else:
        total_cost += heapq.heappop(right_heap)
        if left_ptr < right_ptr:
          right_ptr -= 1
          heapq.heappush(right_heap, costs[right_ptr])

    return total_cost