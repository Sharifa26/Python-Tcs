# https://practice.geeksforgeeks.org/problems/special-series-sum0903/1

def sumOfTheSeries (n):
    return int(n*(n+1)*(n+2)/6)

n=8
print(sumOfTheSeries(n))