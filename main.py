# Calculator app
from art import logo
# Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Dictionary where keys are math symbols: +, -, * and /; values are functions add, sub, multi and divide
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  # Forloop for all the operations(dict) and print them out
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation from the line above: ")
  
  num2 = float(input("What's the second number?: "))
  
  # take operation_symbol and use them on num1 and num2
  answer = operations[operation_symbol](num1, num2)
  
  # print the answer
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  go_math = True
  while go_math:
    decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if decision == "n":
      go_math = False
      calculator()
    else:
      operation_symbol = input("Pick an operation from the line above: ")
      num2 = int(input("What's the next number?: "))
      num1 = answer
      answer = operations[operation_symbol](num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

calculator()