'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_hash = {}

        for i in s1:
            if i not in s2:
                return False
            if i in s1_hash:
                s1_hash[i] = s1_hash[i]+1
            else:
                s1_hash[i]=1
        # print(s1_hash)
        for i in range(len(s2)-len(s1)+1):
            s2_hash = {}
            for j in range(len(s1)):
                if s2[i+j] not in s2_hash:
                    s2_hash[s2[i+j]] = 1
                else:
                    s2_hash[s2[i+j]] = s2_hash[s2[i+j]] + 1
            # print(s2_hash)
            if s1_hash==s2_hash:
                return True

        return False

