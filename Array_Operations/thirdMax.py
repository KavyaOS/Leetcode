class Solution(object):
    def make_unique(self, nums):
        write_pointer = 0
        for read_pointer in range(len(nums)):
            if nums[read_pointer] != nums[write_pointer]:
                write_pointer = write_pointer + 1
                nums[write_pointer] = nums[read_pointer]
        slice_object = slice(write_pointer+1)
        return nums[slice_object]
    
    def thirdMax(self, nums):
        nums.sort()
        nums = self.make_unique(nums)
        if len(nums)>=3:
            return nums[-3]
        else:
            return max(nums)

S = Solution()
nums = [1,2,2,5,3,5]
print(S.thirdMax(nums))