def calculator():
    num1 = float(input("Enter your First Number : "))
    while True:
        print(" + \n - \n * \n / \n")
        operation = input("Select the operation : ")
        num2 = float(input("Enter your Next Number : "))
        # Perfrom calculation : 
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print('Infinity')
                continue
            result == num1 / num2
        else:
            print("Invalid Operation Selected!")
            continue
        # Display the result:
        print(f"Result of {num1} {operation} {num2} = {result}") # Very Critical Thinking
        
        # Ask to continue with the result:
        choice = input(f"Do you want to continue with {result}?(y/n) : ")
        if choice == 'y':
                 num1 = result
        else:
            print("Thank You!")
            break            
        
def display_header():
    print(r"""
   _____      _            _       _             
  / ____|    | |          | |     | |            
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
  _______________________________________________
 |  ___________________________________________  |
 | |                                         | |
 | |    Welcome to the Ultimate Calculator!   | |
 | |_________________________________________| |
 |_____________________________________________|
    """)


# Call the header at the start of your program
display_header()

# Calling Calculator
calculator()
