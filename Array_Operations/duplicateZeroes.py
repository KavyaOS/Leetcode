class Solution(object):
    def duplicateZeros(self, arr):
        for i in reversed(range(0, len(arr)-1)):
            if arr[i] == 0:
                for j in range(len(arr)-1, i, -1):
                    arr[j] = arr[j-1]

S = Solution()
nums = [5, 0, 3, 6, 0, 7, 3]
S.duplicateZeros(nums)
print(nums)