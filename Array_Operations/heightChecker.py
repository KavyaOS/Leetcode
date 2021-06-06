class Solution(object):
    def heightChecker(self, heights):
        not_expected = 0
        actual_heights = heights.copy()
        heights.sort()
        for height_index in range(len(actual_heights)):
            if heights[height_index] != actual_heights[height_index]:
                not_expected = not_expected + 1
                
        return not_expected

S = Solution()
heights = [1,1,4,2,1,3]
print(S.heightChecker(heights))