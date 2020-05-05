'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ind,i in enumerate(s):
            if s.count(i)==1:
                return ind
        return -1

if __name__  == "__main__":
    print(Solution().firstUniqChar('leetcode'))
