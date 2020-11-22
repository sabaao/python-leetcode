class Solution:
    def maxArea(self, height: [int]) -> int:
        result:int = 0
        left:int =0
        right:int = len(height)-1

        while left < right:
            result = max(result, (right-left)*min(height[right],height[left]))
            if height[left] > height[right]:
                right -=1
            else:
                left +=1

        return result
        