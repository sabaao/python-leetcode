class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        count = 0
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if(nums[x]==nums[y] and x<y):
                    count +=1
        return count
