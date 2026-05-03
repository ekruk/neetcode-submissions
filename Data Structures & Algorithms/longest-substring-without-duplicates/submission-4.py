class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # S A B C A X Y Z

        longest_length = 0
        temp_length = 0
        
        dic = {}
        left_window = 0

        for i in range(len(s)):

            if dic.get(s[i]) is None:
                dic[s[i]] = i
                temp_length += 1

            else:
                dyna_window = dic[s[i]]
                while left_window <= dyna_window:
                    del dic[s[left_window]]
                    left_window += 1
                    temp_length -= 1
                dic[s[i]] = i
                temp_length += 1
            longest_length = max(temp_length, longest_length)

        return longest_length





