class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(s)):
            if s_dict[s[i]] != t_dict[t[i]]:
                return False
            
            s_dict[s[i]] = i+1
            t_dict[t[i]] = i+1
        
        return True