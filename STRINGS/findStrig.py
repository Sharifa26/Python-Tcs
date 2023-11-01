def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if  ((string[i : i+len(sub_string)]) == sub_string):
          count = count + 1
    return count
   
string="ABCDCDC"
sub_string="CDC"

print(count_substring(string, sub_string))

"""ans=[[i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if (i+j+k) !=n]
    
    print(ans) """
