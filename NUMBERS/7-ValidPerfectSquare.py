"""Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
"""

import math
def isPerfectSquare(num):
    return math.sqrt(num).is_integer()
num =6
print(isPerfectSquare(num))

