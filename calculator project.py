def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    should_accumalate = True
    num1 = float(input("enter the first number : "))
    
    while should_accumalate :
        for symbol in operations:
            print(symbol)
        operation_symbol = input("select the symbol for operation : ")
        num2 = float(input("enter the second number : "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input("type 'y' to continue with previous answer or type 'n' for new calculation : ")
        
        if choice == "y":
            num1 = answer
            
        else:
            should_accumulate = False
            print("\n" * 40)
            calculator()
calculator()
        
        