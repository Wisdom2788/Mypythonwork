def increasing_numbers():
    

 num1 = int(input("Please enter first number: "))
if (num1 < 0 or num1 > 100):
    print("please input a valid number")
else:
    num1 = int(input("Please enter first number: "))   
num2 = int(input("Please enter a number: "))
if (num2 < 0 or num1 > 100):
    print("Behave and input a valid number")
else:
    num2 = int(input("Please enter second number: "))    
num3 = int(input("Please enter a number: "))
if (num3 < 0 or num1 > 100):
    print("For the last time input a valid number")
else:
    num3 = int(input("Please enter third number: "))    

numbers = [num1, num2, num3]

numbers.sort()

print("output:", ", ".join(map(str, numbers)))
