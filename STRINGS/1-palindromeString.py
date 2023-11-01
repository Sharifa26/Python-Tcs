S= 'abba'

def palindrome(S):
    if(S == S[::-1]):
        return 1
    return 0

print(palindrome(S))
