class Solution(object):
    def lengthOfLIS(self, nums):
        '''Time: O(n^2), Space: O(n)'''
        L = []
        for i in range(len(nums)):
            L.append(1)
        for i in range(1, len(nums)):
            L[i] = 1
            for j in range(i):
                if nums[j]<=nums[i] and L[i]<L[j]+1:
                    L[i] = L[j] + 1
        return max(L)

print(Solution().lengthOfLIS([2, 6, 4, 5, 10]))