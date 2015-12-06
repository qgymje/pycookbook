import heapq

nums = [1, 8, 2, 34, 24, 35, 45, 11, 32, 94]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))