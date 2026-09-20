class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score

# Time: O(n) - 1 loop only
# Space: O(1) - only have score and i