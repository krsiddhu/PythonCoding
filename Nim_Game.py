class Solution:
    def canWinNim(self, n: int) -> bool:
        l = [1,1,1]
        if n<=3:
            return True 
        for i in range(3,n):
            if l[i-1] and l[i-2] and l[i-3]:
                l[i] = 0
            else:
                l[i] =1
        return l[n-1]

s = Solution()
print(s.canWinNim(4))
