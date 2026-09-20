class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)): # for each word in words, example: words[0] = "abcd"
            for j in range(len(words[i])): # for each char in words
                if j >= len(words): 
                    return False
                if i >= len(words[j]):
                    return False
                if words[i][j] != words[j][i]:
                    return False
        return True
         