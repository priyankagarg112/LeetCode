'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.



Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.
'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return self.find_ele(nums,0,len(nums)-1)

    def find_ele(self,nums,l,h):
        if l>h:
            return
        if l==h:
            return nums[l]
        mid = l+((h-l)//2)
        if nums[mid]==nums[mid-1]:
            if mid % 2==1:
                return self.find_ele(nums,mid+1,h)
            return self.find_ele(nums,l,mid-1)
        elif nums[mid]==nums[mid+1]:
            if mid % 2==1:
                return self.find_ele(nums,l,mid-1)
            return self.find_ele(nums,mid+1,h)
        else:
            return self.find_ele(nums,mid,mid)
