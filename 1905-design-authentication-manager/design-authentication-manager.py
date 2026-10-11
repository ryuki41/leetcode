class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.token = dict()
        self.time = timeToLive    # 有効期間（timeToLive）を保存し、トークン管理用の空の辞書を作成する

    def generate(self, tokenId, currentTime):
        self.token[tokenId] = currentTime    # 指定されたトークンIDと作成（生成）時刻を辞書に保存する

    def renew(self, tokenId, currentTime):
        limit = currentTime - self.time        # 有効期限の基準となる限界時刻を計算する（これより古いと期限切れ）
        if tokenId in self.token and self.token[tokenId] > limit:    # トークンが存在し、かつ有効期限内の場合のみ
            self.token[tokenId] = currentTime                        # トークンの時刻を現在時刻に更新する

    def countUnexpiredTokens(self, currentTime):
        limit = currentTime - self.time       # 有効期限の基準となる限界時刻を計算する
        c = 0
        for i in self.token:
            if self.token[i] > limit:         # トークンが有効期限内の場合は
                c += 1                        # カウントを1増やす
        return c