class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        result = []
        count = 0

        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j :
                    continue
                if nums[i] > nums[j]:
                    count += 1

            result.append(count)
            count = 0

        return result