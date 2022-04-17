class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1
        answer = 0
        while i < j:
            answer = numbers[i] + numbers[j]
            if answer == target:
                return [i+1,j+1]
            if answer<target: i+=1
            else: j-=1

print(Solution().twoSum([2, 7, 11, 15], 9))