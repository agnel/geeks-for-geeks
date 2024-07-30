# Maximum value of |arr[i] – arr[j]| + |i – j|
# Ref: https://www.geeksforgeeks.org/maximum-value-arri-arrj-j/?ref=agnelwaghela
# Given a array of N positive integers. The task is to find the maximum value of |arr[i] – arr[j]| + |i – j|, where 0 <= i, j <= N – 1 and arr[i], arr[j] belong to the array.
# Examples:
# Input : N = 4, arr[] = { 1, 2, 3, 1 } 
# Output : 4
# Explanation:
# Choose i = 0 and j = 2. This will result in |1-3|+|0-2| = 4 which is the maximum possible value.
# Input : N = 3, arr[] = { 1, 1, 1 }
# Output : 2

import sys

def findValue(arr, n):
  max_X = -sys.maxsize
  min_Y = sys.maxsize
  max_M = -sys.maxsize
  min_N = sys.maxsize

  for i in range(n):
    X = arr[i] + i
    M = arr[i] - i
    max_X = max(max_X, X)
    min_Y = min(min_Y, X)
    max_M = max(max_M, M)
    min_N = min(min_N, M)

  return max(max_X - min_Y, max_M - min_N)
