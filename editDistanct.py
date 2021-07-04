class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def findMinDistance(word1, x, word2, y):

            if x < 0 and y < 0:
                return 0

            if y < 0:
                return len(word1[:x+1])
            if x < 0:
                return len(word2[:y+1])

            if word1[x] == word2[y]:
                return findMinDistance(word1, x - 1, word2, y - 1)

            return 1 + min(findMinDistance(word1, x, word2, y - 1), findMinDistance(word1, x - 1, word2, y),
                           findMinDistance(word1, x - 1, word2, y - 1))

        return findMinDistance(word1, len(word1) - 1, word2, len(word2) - 1)


print(Solution().minDistance('abc','bcd'))