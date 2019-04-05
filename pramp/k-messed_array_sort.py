from heapq import heapify, heappop, heappush
def sort_k_messed_array(arr, k):
  if k == 0: return arr
  heap = arr[:k+1]
  heapify(heap)
  for i, element in enumerate(arr[k+1:]):
    smallest = heappop(heap)
    heappush(heap, element)
    arr[i] = smallest
  for i in range(len(arr)-k-1, len(arr)):
    arr[i] = heappop(heap)
  return arr

# O(log(k))
# space: O(k)