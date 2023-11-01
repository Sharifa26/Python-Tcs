"""Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
"""
num=33

def add(num):
   if num == 0 : return 0
   if num % 9 == 0 : return 9
   else : return (num % 9)

print(add(num))


