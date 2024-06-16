#The calculator using python 
import operator


A = int(input("enter the input for no : 1 => "))
B = int(input("enter the input for no : 2 => "))
c = str(input("enter the input for operation : +,-,*,%,/"))

if c == '+':
  print(operator.add(A,B))
elif c == "-":
  print(operator.sub(A,B))
elif c == "*":
  print(operator.mul(A,B))
elif c== "/":
  print(operator.div(A,B))
elif c == "%":
  print(operator.mod (A,B))
else:
  print("Invalid opeartor")
