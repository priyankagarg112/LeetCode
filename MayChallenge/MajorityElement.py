'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
from typing import List

#Solution1:


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


#Solution2:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        visited = []
        for i in nums:
            if i in visited:
                continue
            if nums.count(i) > (len(nums)/2):
                return i
            visited.append(i)


if __name__ == "__main__":
    print(Solution().majorityElement([3,1,3,2,3]))
