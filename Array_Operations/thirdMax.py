class Solution(object):
    def make_unique(self, nums):
        write_pointer = 0
        nums1 = []
        for read_pointer in range(0, len(nums)):
            if nums[read_pointer] != nums1[write_pointer]:
                nums1[write_pointer] = nums[read_pointer]
                write_pointer = write_pointer + 1
        return nums1
    
    def thirdMax(self, nums):
        nums1 = self.make_unique(nums)
        nums1.sort()
        if len(nums1) >= 3:
            return nums1[2]
        else:
            return nums1[len(nums1)-1]

S = Solution()
nums = [2,2,3,1]
print(S.thirdMax(nums))