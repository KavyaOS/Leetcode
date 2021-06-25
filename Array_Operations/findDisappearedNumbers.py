class Solution(object):
    def findDisappearedNumbers(self, nums):
        return set(range(1,len(nums)+1))-set(nums)

S = Solution()
nums = [1,1]
print(S.findDisappearedNumbers(nums))