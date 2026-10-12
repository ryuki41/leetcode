class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.token = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime        

    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime - self.ttl
        
        if tokenId in self.token and self.token[tokenId] > limit:
            self.token[tokenId] = currentTime  

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for tokenId in self.token:
            limit = currentTime - self.ttl
            if self.token[tokenId] > limit:
                count += 1
        
        return count
            
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)