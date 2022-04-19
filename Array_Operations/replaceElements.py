class Solution(object):
    def replaceElements(self, arr):
        '''max = 0
        for i in range(len(arr)-1):
            max = 0
            for j in range(i+1,len(arr)):
                if arr[j]>max:
                    max = arr[j]
            arr[i] = max
        arr[len(arr)-1] = -1'''
        max = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for i in reversed(range(len(arr)-1)):
            temp = arr[i]
            arr[i] = max
            if temp > max:
                max = temp

S = Solution()
arr = [17,18,5,4,6,1]
S.replaceElements(arr)
print(arr)