'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters
'''

from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq_dict = defaultdict(int)
        for i in s:
            freq_dict[i] +=1
        if len(freq_dict)==1:
            return s
        
        chars = list(freq_dict.keys())
        
        for i in range(len(chars)//2-1,-1,-1):
            self._heapify(chars,i,len(chars),freq_dict)
        
        result = ''
        for i in range(len(chars)-1,-1,-1):
            result = result + chars[0]*freq_dict[chars[0]]
            chars[0],chars[i]=chars[i],chars[0]
            self._heapify(chars,0,i,freq_dict)
            
        return result
        
    
    def _heapify(self,arr,i,n,freq_dict):
        largest = i
        left_child = 2*i + 1
        right_child = 2*i + 2
        
        if left_child < n and freq_dict[arr[largest]] < freq_dict[arr[left_child]]:
            largest = left_child
        
        if right_child < n and freq_dict[arr[right_child]] > freq_dict[arr[largest]]:
            largest = right_child
        
        if i != largest:
            arr[largest],arr[i]=arr[i],arr[largest]
            self._heapify(arr,largest,n,freq_dict)
        
        
        
        
            
        
