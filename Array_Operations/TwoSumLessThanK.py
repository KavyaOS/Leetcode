class Solution(object):
    def twoSumLessThanK(self, nums, k):
        # sum_ij = -1
        # for j in range(1, len(nums)):
        #     for i in range(j):
        #         if nums[i]+nums[j]>sum_ij and nums[i]+nums[j]<k:
        #             sum_ij = nums[i]+nums[j]
        # return sum_ij

        answer = -1
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        print(nums)
        while i<j:
            if nums[i] + nums[j] < k:
                answer = max(answer, nums[i]+nums[j])
                i+=1
            else:
                j-=1
        return answer

print(Solution().twoSumLessThanK([254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
, 200))