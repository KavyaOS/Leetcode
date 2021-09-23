'''https://leetcode.com/problems/majority-element/'''

class Solution(object):
    def majorityElement(self, nums):
        if(len(nums)%2!=0):
            key = nums[len(nums)-1]
            count = nums.count(key)
            '''for num in nums:
                if key == num:
                    count = count + 1'''
            if count > (len(nums)//2):
                return key
            nums.pop()
        if nums is None:
            return nums
        if len(nums)==1:
            return nums[0]
        B = []
        for i in range(0, len(nums)-1, 2):
            if nums[i]==nums[i+1]:
                B.append(nums[i])

        if B: return self.majorityElement(B)
        else: return None

nums = [2, 2, 3]
S = Solution()
print(S.majorityElement(nums))