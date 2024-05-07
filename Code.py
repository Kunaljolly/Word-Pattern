class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        d = {}
        reverse_d = {}
        t = s.split(" ")
        
        if len(p) != len(t):
            return False
        
        for x in range(len(p)):
            if p[x] in d:
                if d[p[x]] != t[x]:
                    return False
            else:
                if t[x] in reverse_d:
                    return False
                d[p[x]] = t[x]
                reverse_d[t[x]] = p[x]
        return True
