'''Brute Force Approach'''
class Naive_Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    return [i, j]

'''Time:O(n), space:O(1)'''
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

print(Solution().twoSum([2,7,11,15], 9))