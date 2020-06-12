'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=r=0
        n=len(nums)
        b=n-1
        while i <= b:
            if nums[i] == 0:
                nums[i],nums[r]=nums[r],nums[i]
                r +=1

            elif nums[i]==2:
                nums[i],nums[b] = nums[b],nums[i]
                b -= 1
                i -= 1
            print(nums)
            i += 1

