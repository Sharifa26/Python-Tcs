n=2

# for num in range(n+1):
#    # all prime numbers are greater than 1
#    if num > 0:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, (n*n) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(n))