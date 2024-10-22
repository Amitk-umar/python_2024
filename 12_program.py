def factorial(num):
    if num == 1:
        return num
    else:
        return (num * factorial(num - 1))


n = int(input("Enter the number to find factorial of: "))
print("Factorial is: ", factorial(n))
