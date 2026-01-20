import sys
def add(num1, num2):
    answer = num1 + num2
    return answer

def sub(num1, num2):

    answer = num1 - num2
    return answer

def mult(num1, num2):
    answer = num1 * num2
    return answer

def div(num1, num2):
    answer = num1 / num2
    return answer
while True:
    operation = input("Enter the operation required: \n1 = addition\n2 = subtraction\n3 = multiplication\n4 = division\n9 = exit\n")


    #num1 = int(input("Enter the first number: "))
    #num2 = int(input("Enter the second number: "))

    match operation:
         case "1":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                answer = add(num1, num2)
                print(answer)
         case "2":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                answer = sub (num1, num2)
                print(answer)
         case "3":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             answer = mult(num1, num2)
             print(answer)
         case "4":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             answer = div(num1, num2)
             print(answer)
         case "9":
             sys.exit(0)