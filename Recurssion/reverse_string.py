class Solution(object):
    '''Space: O(1), Time: O(len(input_string)/2)'''
    def reverseString(self, s):
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
     
s = ["h","e","l","l","o"]
S = Solution()
S.reverseString(s)
print(s)