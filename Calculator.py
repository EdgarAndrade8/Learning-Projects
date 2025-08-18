def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calc():
    selectedOperation = input("Do you wish to:\n+\n-\n*\n/\n")
    while selectedOperation not in operations:
        print("Please select a valid command.")
        selectedOperation = input("Do you wish to:\n+\n-\n*\n/\n")
    operation = operations[selectedOperation]
    n2 = float(input("Insert second number:\n"))
    return operation(n1, n2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

wantsToContinue = ""
calculator = True
wantsToRestart = True
restart = True
while restart:
    n1 = float(input("Please, insert first number:\n"))
    while calculator:
        value = calc()
        print(value)
        calculator = False
        restart = False

        wantsToContinue = input("Do you wish to continue with this value?\n"
                                "'y' for Yes or 'n' for No.\n").lower()
        if wantsToContinue == "y":
            calculator = True
            n1 = value
        elif wantsToContinue == "n":
            wantsToRestart = input("Do you wish to restart the calculator?\n"
                                   "'y' for Yes or 'n' for No.\n").lower()
    if wantsToRestart == "y":
        restart = True
    elif wantsToRestart == "n":
        print("Goodbye!")

    calculator = True
