def main():
    problem1()
    # problem2()


# Create a function that has a loop that quits with q. If the user doesn't enter q, ask them to input another string.
# # BONUS: Make sure the code can handle whatever case the User enters the q as (uppercase or lowercase).
def problem1():
    while (True):
        userInput = input("Enter something, Enter q to quit ")
        # print(userInput.upper())
        if userInput.upper() == "Q":
            break
    

# Write 2 functions: exercise2() and exercise2_helper(num1, num2, num3. operation)
# The function exercise2_helper(num1, num2, num3) should expect 3 numbers, 
# and an operation to perform as a String as parameters.
# The function should support 3 operations:
# SUM - Return the sum of the 3 numbers
# PROD - Return the product of the 3 numbers
# AVG - Return the average of the 3 numbers
# The operation and the returned value should then be printed out back in the main exercise2() function. Return INVALID OPERATION if an operation passed in that isn't supported. HINT: Use switch/case
def problem2():
    num1= int(input("Enter number 1 "))
    num2 = int(input("Enter number 2 "))
    num3 = int(input("Enter number 3 "))
    userOp = input("Enter 1 of 3 operations: sum, prod, or avg ")
    def exercise(num1,num2,num3,op):
        add = num1 + num2 + num3
       
        if (op == "sum"):
            print(num1 + num2 + num3)
        elif (op == "prod"):
            print(num1 * num2 * num3)
        elif (op == "avg"):
            print(add // 3)
        else: print("INVALID OPERATION")
     

    exercise(num1,num2,num3,userOp)

if __name__ == '__main__':
    main()