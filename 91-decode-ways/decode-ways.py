class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        # dp[i]: i文字目までで何通りのデコードパターンがあるか
        dp = [0 for _ in range(N+1)]

        # 0文字目までには1通りのデコードパターンがある（空文字列にデコードできる）
        # よってここは0ではなく1であることに注意！
        dp[0] = 1

        for i in range(1, N+1):
            # 1桁のcode
            code1 = s[i-1]     
            # code1に対応するアルファベットが存在する
            # i番目の文字をそのアルファベットでデコードすれば良いだけなので、dp[i-1]通りある
            if "1" <= code1 and code1 <= "9":
                dp[i] += dp[i-1]

            if i > 1:
                # 2桁のcode
                code2 = s[i-2:i]
                # code2に対応するアルファベットが存在する
                # i-1とi-2番目の文字が連なったコードをアルファベットにデコードすれば良いだけなので、dp[i-2]通りある
                if "10" <= code2 and code2 <= "26":
                    dp[i] += dp[i-2]

        return dp[N]