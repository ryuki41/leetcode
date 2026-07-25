class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_list = defaultdict(list)
        for value in strs:
            # 小文字英字の各文字の出現回数のカウンター
            counter = [0] * 26
            for s in value:
                counter[ord(s) - ord("a")] += 1

            counter_list[tuple(counter)].append(value)

        return list(counter_list.values())



        