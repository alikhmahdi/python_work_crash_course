try:
    num1 , num2 = int(input("Enter two numbers separated by a space:\n")), int(input())
except ValueError:
    print("Invalid input. Please enter two numbers.")
else:
    print("The sum is:", num1 + num2)