# sys is a module used to read command line arguments
import sys

def add(num1,numm2):
    res = num1 + numm2
    return res

def mul(num1, num2):
    res = num1 * num2
    return res

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = add(num1,num2)
    print(output)