class Solution(object):
    def removeDuplicates(self, nums):
        j=0
        for i in range(len(1, nums)):
            if(nums[i]!=nums[j]):
                j = j+1
                nums[j] = nums[i]
        return j+1

S = Solution()
nums = [1, 2, 2, 5, 8, 8]
n = S.removeDuplicates(nums)
for i in range(n):
    print(nums[i])