class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_list = [0] * 26

        for i in range(len(magazine)):
            m_list[ord(magazine[i]) - ord("a")] += 1
        
        for i in range(len(ransomNote)):
            if m_list[ord(ransomNote[i]) - ord("a")] == 0:
                return False
            m_list[ord(ransomNote[i]) - ord("a")] -= 1
        
        return True

