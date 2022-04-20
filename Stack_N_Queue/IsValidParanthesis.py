class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch in ['(','[','{']:
                stack.append(ch)
            elif ch in [')', ']', '}']:
                if len(stack) == 0:
                    return False
                if ch == ')' and stack.pop() != '(':
                    return False
                elif ch == ']' and stack.pop() != '[':
                    return False
                elif ch == '}' and stack.pop() != '{':
                    return False
        
        return stack == []

print(Solution().isValid("(([))"))