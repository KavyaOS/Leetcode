class Solution(object):
    def removeElement(self, nums, val):
        '''counter = 0
        for i in range(len(nums)):
            if nums[i] == val:
                temp = nums[i]
                for j in range(i, len(nums)-counter-1):
                    nums[j] = nums[j+1]
                    counter = counter + 1
                nums[j] = temp
                
        return counter-1'''
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i = i+1
                
        return i

S = Solution()
nums = [0,1,2,2,3,0,4,2]
count = S.removeElement(nums,2)
for i in range(count):
    print(nums[i])