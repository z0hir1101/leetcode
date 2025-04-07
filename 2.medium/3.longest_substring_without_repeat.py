class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = [0] * 128
        maxln = begin = 0

        for i in range(len(s)):
            if begin < index[ord(s[i])]:
                begin = index[ord(s[i])]
            index[ord(s[i])] = i + 1
			
            if maxln <= i - begin + 1:
                maxln = i - begin + 1
        return maxln

s = input()
print(Solution.lengthOfLongestSubstring(None, s))
                
