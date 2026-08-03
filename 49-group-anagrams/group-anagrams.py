class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for st in strs:
            counter = [0] * 26
            for c in st:
                counter[ord(c) - ord("a")] += 1

            groups[tuple(counter)].append(st)
        
        return list(groups.values())