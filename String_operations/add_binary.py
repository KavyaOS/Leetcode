class Solution(object):
    def addBinary(self, a, b):
        num1 = 0
        num2 = 0
        total = 0
        k = 0
        l = 0
        result = ''
        for i in reversed(range(len(a))):
            num1 = num1 + int(a[i])*pow(2,k)
            k = k + 1
            
        for j in reversed(range(len(b))):
            num2 = num2 + int(b[j])*pow(2,l)
            l=l+1
            
        total = num1 + num2
        while total!=0:
            result = result + str(total%2)
            total = total//2
            
        return result[::-1] if result else "0"

print(Solution().addBinary('1010','1011'))