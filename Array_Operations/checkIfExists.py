class Solution(object):
    def checkIfExist(self, arr):
        dict = {}
        for i in range(len(arr)):
            #if ((arr[i] // 2) in dict.values() and (arr[i] % 2) == 0) or (arr[i] * 2) in dict.values():
            #    return True
            #dict[i] = arr[i]
            
            val = 2 * arr[i]
            for j in range(i):
                if arr[j]==val:
                    return True
            for j in range(i+1, len(arr)):
                if arr[j]==val:
                    return True
        return False

S = Solution()
arr = [2, 5]
print(S.checkIfExist(arr))