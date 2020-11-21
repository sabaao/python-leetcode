class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_count = 0

        for i in s:
            if i in str_list:
                str_list = str_list[str_list.index(i) + 1 :]
            str_list.append(i)
            max_count = max(max_count,len(str_list))
        return max_count