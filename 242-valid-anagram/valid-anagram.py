class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for v in s:
            s_dict[v] +=1

        for w in t:
            t_dict[w] += 1

        return s_dict == t_dict    