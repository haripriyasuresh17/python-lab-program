# palindrome
number = int(input("Enter an integer number: "))

if number % 2 == 1:  
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    
    num_digits = len(str(factorial))
    
    print("Factorial:", factorial)
    print("Number of digits in factorial:", num_digits)
else:  
    num_str = str(number)
    if num_str == num_str[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
