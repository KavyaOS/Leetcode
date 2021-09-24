import timeit

class Solution(object):
    '''Space: O(1), Time: O(len(input_string)/2)'''
    def reverseString_iterative(self, s):
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
    
    def reverseString_recursive(self, s):
        '''Space: O(1), time: O(n)'''
        self.reverse(s, 0, len(s)-1)

    def reverse(self, s, begin, end):
        if begin>=end:
            return
        temp = s[begin]
        s[begin] = s[end]
        s[end] = temp
        self.reverse(s, begin+1, end-1)

"""s = ['h', 'e', 'l', 'l', 'o']"""
s = ['h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','h', 'e', 'l', 'l', 'o','1','2']
S = Solution()
start = {timeit.timeit(number = 10000000)}
S.reverseString_recursive(s)
end = {timeit.timeit(
    number = 10000000)}
print(start-end)
print(s)