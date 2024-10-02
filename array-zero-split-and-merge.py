# Check whether an Array can be made 0 by splitting and merging repeatedly
# Ref: https://www.geeksforgeeks.org/check-whether-an-array-can-be-made-0-by-splitting-and-merging-repeatedly/
# tags: bca, day-6, bit-manipulation, array-zero-split-and-merge, xor
class ArrayZeroSplitAndMerge:
    def __init__(self, arr):
        self.arr = arr
        
    def check(self):
        arr = self.arr
        odds_count = 0

        for i in range(len(arr)):
            odds_count ^= arr[i]
        

        return not (odds_count % 2)
