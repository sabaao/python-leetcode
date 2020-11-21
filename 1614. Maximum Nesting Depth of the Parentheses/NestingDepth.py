class Solution:
    def maxDepth(self, s: str) -> int:
        maxCount = 0
        count = 0
        for s in str:
            if s=="("):
                count +=1
                if count > maxCount:
                    maxCount = count
            elif s==")":
                count -=1
        return maxCount
