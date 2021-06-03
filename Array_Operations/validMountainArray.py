class Solution(object):
    def validMountainArray(self, arr):
        increasing, decreasing = False, False
        i = 0
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                increasing = True
            else:
                break
        for j in range(i, len(arr)-1):
            if arr[j+1] < arr[j]:
                decreasing = True
            else:
                decreasing = False
                break
                
        return increasing and decreasing

S = Solution()
arr = [3,7,6,4,3,0,1,0]
#arr = [0, 3, 2, 1]
print(S.validMountainArray(arr))