# ### 2. Simple Calculator

# **Description**: Basic arithmetic operations with user input.

# **Practice Goals**:
# - Function creation and organization
# - Error handling for invalid operations
# - Menu-driven program structure

# user input validation
def check_input(input):
    try:
        val = float(input)
        return val
    except ValueError:
        print("Invalid input!")
        return 0

# get a number from user
value = check_input(input("Calculator.\n Enter value: "))

def add():
    global value
    by = check_input(input(f"\n add {value} by: "))
    value += by
    main_menu()

def subtract():
    global value
    by = check_input(input(f"\n subtract {value} by: "))
    value -= by
    main_menu()

def multiply():
    global value
    by = check_input(input(f"\n multiply {value} by: "))
    value *= by
    main_menu()

def divide():
    global value
    by = check_input(input(f"\n divide {value} by: "))
    value /= by
    main_menu()

def exponent():
    global value
    by = check_input(input(f"\n exponent {value} by: "))
    value **= by
    main_menu()

# user menu option checking
def main_menu_option(option):
    if option in ["1", "+", "add", "Add"]:
        add()
    elif option in ["2", "-", "subtract", "Subtract"]:
        subtract()
    elif option in ["3", "*", "multiply", "Multiply"]:
        multiply()
    elif option in ["4", "/", "divide", "Divide"]:
        divide()
    elif option in ["5", "^", "exponent", "Exponent"]:
        exponent()
    elif option in ["6", "clear", "Clear"]:
        global value
        value = 0
        main_menu()
    elif option in ["7", "exit", "Exit"]:
        print("\n Goodbye!")
        return
    else:
        print("Invalid option!")
        main_menu()

# calculator main menu
def main_menu():
    print(f"\n Current value: {value}")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exponent")
    print("6. clear")
    print("7. exit")
    main_menu_option(input())

main_menu()