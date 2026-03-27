def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))
print("Factorial of -1:", factorial(-1))
print("\nFactorial of 5:", factorial(0))