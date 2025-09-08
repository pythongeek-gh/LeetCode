# Sources: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/editorial/ 
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for n1 in range(1, n):
            n2 = n - n1
            if "0" not in str(n1) + str(n2):
                return [n1, n2]

