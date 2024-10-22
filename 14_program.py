# Fibonacci function using recursion
def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)

# Main program for Fibonacci series
n = int(input("Enter the number of terms needed: "))
for i in range(n):  # Fixed indentation issue here
    print(fib(i))

# NEW MODULE (if you want to separate into a different module)
# Ensure p14.py has the following function definition
import p14

# Assuming p14 has a function fib
num = int(input("Enter any number to print Fibonacci series: "))
p14.fib(num)  # Corrected the reference to p14 instead of 'fibonacci'
