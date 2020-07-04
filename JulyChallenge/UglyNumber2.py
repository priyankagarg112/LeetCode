'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [i+1 for i in range(n)]
        ugly[0]=1
        i2 = i3 = i5 = 0

        for i in range(1,n):
            new_no = min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)
            ugly[i]=new_no
            if new_no == ugly[i2]*2:
                i2 +=1
            if new_no == ugly[i3]*3:
                i3 +=1
            if new_no == ugly[i5]*5:
                i5 +=1

        return new_no
