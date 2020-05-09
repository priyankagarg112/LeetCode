'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        return self.check(0,(num//2+1),num)

    def check(self,l,h,num):
        if l>h:
            return False
        mid = l+(h-l)//2
        # print(l,h,mid)
        if mid**2 == num:
            return True
        if mid**2 > num:
            return self.check(l,mid-1,num)
        else:
            return self.check(mid+1,h,num)

if __name__ == "__main__":
    print(Solution().isPerfectSquare(8))
