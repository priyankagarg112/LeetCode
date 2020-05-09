'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
'''

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        org = None
        for i in range(0, len(coordinates)-1, 2):
            if abs(coordinates[i][0] - coordinates[i+1][0]) == 0:
                if org:
                    if org == -1:
                        continue
                    else:
                        return False
                else:
                    org = -1
            else:
                s = abs(coordinates[i][1] - coordinates[i+1][1]) / abs(coordinates[i][0] - coordinates[i+1][0])
                if org:
                    if org == s:
                        continue
                    else:
                        return False
                else:
                    org = s
        return True

if __name__ == "__main__":
    print(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
