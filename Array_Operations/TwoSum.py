class Solution:
    def twoSum(self, nums, target):
        hashmap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
        return -1

print(Solution().twoSum([-1,2,1,-4], 1))
            