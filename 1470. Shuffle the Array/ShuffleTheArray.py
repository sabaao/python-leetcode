class Solution:
    def shuffle(self, nums: [int], n: int) -> [int]:
        xArray = []
        yArray = []
        resultArray = []

        for i in range(0,n):
            xArray.append(nums[i])
        for i in range(n,n*2):
            yArray.append(nums[i])
        
        for i in range(0,n):
            resultArray.append(xArray[i])
            resultArray.append(yArray[i])
        return resultArray