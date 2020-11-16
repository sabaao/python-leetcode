class Solution:
    def decompressRLElist(self, nums: [int]) -> [int]:
        self.result = []
        for i in range(0,len(nums),2) :
            self.result.append(nums[i] * [nums[i+1]])
        
        return [item for sublist in self.result for item in sublist]
