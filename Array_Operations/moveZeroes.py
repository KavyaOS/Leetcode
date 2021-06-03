class Solution(object):
    def moveZeroes(self, nums):
        writePointer = 0
        for readPointer in range(len(nums)):
            if nums[readPointer] != 0:
                nums[writePointer] = nums[readPointer]
                writePointer = writePointer + 1

        while writePointer!=len(nums) :
            nums[writePointer] = 0
            writePointer = writePointer + 1

S = Solution()
nums = [0,1,0,3,12]
S.moveZeroes(nums)
print(nums)