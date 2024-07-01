class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split(" ")        
        if len(pattern) != len(split_s):
            return False
        else:
            dic = {}
            for i,p in enumerate(pattern):
                if p not in dic:
                    if split_s[i] in dic.values():
                        return False
                    dic[p] = split_s[i]
                elif dic[p] != split_s[i]:
                    return False 
            return True     

s = Solution()
print(s.wordPattern("abba","dog dog dog dog"))
