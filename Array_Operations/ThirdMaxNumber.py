class Solution(object):
    def thirdMax(self, nums):
        max_nums = set()
        for i in range(len(nums)):
            max_nums.add(nums[i])
            if len(max_nums)>3:
                max_nums.remove(min(max_nums))
        if len(max_nums)<3:
            return max(max_nums)
        return min(max_nums)

print(Solution().thirdMax([3,2,1]))