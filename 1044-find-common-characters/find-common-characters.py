class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter_list = []
        for word in words:
            # 各小文字英字のカウントを数える
            counter = [0] * 26
            for w in word:
                counter[ord(w)- ord("a")] += 1
            counter_list.append(counter)

        duplicate_list = []
        for index in range(26):
            str_list = []
            for counter in counter_list:
                str_list.append(counter[index])
                
            # 各単語に何回指定のアルファベットが出てくるかの最小値を取得
            str_min = min(str_list)

            for i in range(str_min):
                duplicate_list.append(chr(index+ord("a")))
        
        return duplicate_list
