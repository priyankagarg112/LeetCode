'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
'''

from random import random

class Solution:

    def __init__(self, w: List[int]):
        self.p = []
        s=0
        for i in range(len(w)):
            s +=w[i]
            self.p.append(s)
        self.sum = sum(w)


    def pickIndex(self) -> int:
        n=random()*self.sum
        l,h=0,len(self.p)
        while l<h:
            m = l+((h-l)//2)
            if self.p[m]>n:
                h=m
            else:
                l=m+1
        return h
