class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, o in enumerate(order):
            order_map[o] = index

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            min_len = min(len(w1), len(w2))
           
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return False
                
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break

        return True

            

        