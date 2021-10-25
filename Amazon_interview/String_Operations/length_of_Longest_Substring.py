class Naive_Solution(object):
    '''Time: O(n^3), Space: )(n)'''
    def lengthOfLongestSubstring(self, s):
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.check(s, i, j):
                    result = max(result, j-i+1)
        return result
                    
    def check(self, s, start, end):
        hashmap = {}
        for i in range(start, end+1):
            if s[i] in hashmap:
                return False
            hashmap[s[i]] = i
        return True

'''Sliding window approach: Time: O(n), space: O(n)'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = {}
        left = right = 0
        result = 0
        while right<len(s):
            if s[right] in char_set:
                char_set[s[right]] = char_set[s[right]] + 1
            else: char_set[s[right]] = 1
            
            while(char_set[s[right]]>1):
                char_set[s[left]] = char_set[s[left]] - 1
                left = left + 1
                
            result = max(result, right - left + 1)
            
            right = right + 1
        return result

print(Solution().lengthOfLongestSubstring("abcabcbb"))