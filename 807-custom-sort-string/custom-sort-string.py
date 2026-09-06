class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = defaultdict(int)
        for i, o in enumerate(order):
            order_map[o] = i
        
        return "".join(sorted(s, key=lambda c: order_map[c]))
