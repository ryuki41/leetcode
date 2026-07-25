class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic_order = defaultdict(int)
        for index, v in enumerate(order):
            dic_order[v] = index
        
        return "".join(sorted(s, key=lambda o: dic_order[o]))