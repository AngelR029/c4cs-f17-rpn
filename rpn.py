#!/usr/bin/env python3

import operator
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

mode = {
    "log": False,        
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        if token in mode:
            if mode[token]:
                mode[token] = False
            else:
                mode[token] = True
        else: 
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        if mode["log"]:
            print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
