def nth_fibonacci(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return nth_fibonacci(n-1)+nth_fibonacci(n-2)

n = int(input("Enter value of n : "))
print("nth fibonacci number with n = {} is {}".format(n, nth_fibonacci(n)))
