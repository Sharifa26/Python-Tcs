# https://practice.geeksforgeeks.org/problems/consonants-and-vowels-check/1

"""
Input:s = "aaaaaa"
Output:Yes
"""
def checkString(s):
    vowels=0
    const=0
    l=0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='u' or i=='o'):
            vowels +=1
        elif(i=='' or i ==' '):
            l +=1
        else:
            const +=1
    if( vowels > const):
        print("Yes")
    elif( vowels < const):
        print("No")
    elif( vowels == const):
        print("Same")
s = "aaaaaa"
print(checkString(s))