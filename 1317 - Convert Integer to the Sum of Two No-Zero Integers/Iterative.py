# Sources: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/solutions/7167093/o-log-n-time-intuitive-step-by-step-method/
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        n1, n2 = 0, 0
        pos = 1

        while n > 0:
            num = n % 10
            if num == 0:
                n1 += 1 * pos
                n2 += 9 * pos
                n -= 10
            elif num == 1 and n >= 10:
                n1 += 2 * pos
                n2 += 9 * pos
                n -= 10
            else:
                n1 += (num - 1) * pos
                n2 += 1 * pos
            n //= 10
            pos *= 10
        
        return [n1, n2]

