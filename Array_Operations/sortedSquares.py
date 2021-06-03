class Solution(object):
    def __init__(self) -> None:
        super().__init__()

    def sortedSquares(self, nums):
        nums = [num**2 for num in nums]
        print(nums)
        nums.sort()
        # print(nums)
        return nums

S = Solution()
nums = [0, 1 , 2, 8, 6]
print(S.sortedSquares(nums))