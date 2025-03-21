# This problem can be solved by using two different approaches with different complexities

# Optimized solution (needs merge sort implementation; skipped implementing from scratch)
from sortedcontainers import SortedList

def total_inversions(arr):
    inv_count = 0
    sorted_list = SortedList()

    for num in arr:
        inv_count += len(sorted_list) - sorted_list.bisect_right(num)
        sorted_list.add(num)

    return inv_count

# Brute force (trivial solution: not efficient, O(n^2) solution)
def brute_force(arr):
    n = len(arr)
    inversion_count = 0

    # Iterate through all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversion_count += 1

    return inversion_count

arr = [1,40,6,4,5]
print(f"total inversions optimal: {total_inversions(arr)}, total inversion bruteforce: {brute_force(arr)}")
