class Solution:
    def restoreString(self, s: str, indices: [int]) -> str:
        result =""
        for i in range(0,len(indices)):
            result += s[indices.index(i)]
        return result