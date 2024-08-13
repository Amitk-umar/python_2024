#write a program to find Prime number

number = int(input("Enter a number: "))

if number == 1:
    print("1 is a unit number.")
    

elif number > 1:
   
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is a composite number.")
else:
    print(f"{number} is neither prime, composite, nor a unit number.")




# #write a program to find Prime number using functon
# def check_number_type(number):
#     if number <= 0:
#         return "Neither prime, composite, nor unit."
#     elif number == 1:
#         return "1 is a unit number."
#     elif number == 2:
#         return "2 is a prime number."
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 return f"{number} is a composite number."
#         return f"{number} is a prime number."

# # Test the function
# num = int(input("Enter a number: "))
# result = check_number_type(num)
# print(result)



# #write a program to find Prime number using function
# def check_number_type(number):
#     if number == 1:
#         return "1 is a unit number."
#     elif number == 2:
#         return "2 is a prime number."
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 return f"{number} is a composite number."
#         return f"{number} is a prime number."

# # Iterate through the range 2 to 100
# for num in range(2, 101):
#     result = check_number_type(num)
#     print(result)

