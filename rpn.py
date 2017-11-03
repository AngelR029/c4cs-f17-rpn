#!/usr/bin/env python3

import operator
import readline
from termcolor import colored, cprint
import colorama

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

mode = {
    "log": False,        
    "color": True,
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
                
                if len(stack) == 0:
                    raise TypeError("Too many operators")
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        if(len(stack) > 0): 
            if mode["log"]:
                if mode["color"]:
                    for number in stack:
                        if number < 0:
                            print('['+ colored(number, "red") + ']', end='')
                        else :
                            print('[' + colored(number, 'green') + ']', end='')
                    print()
                else:
                    print(stack)
    if len(stack) == 0:
        return None
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> ")) 
        if result == None:
            pass
        else:
            if mode["color"]: 
                if result < 0:
                    print("result> " + colored(result, "red"))
                else :
                    print("result> " + colored(result, 'green'))
            else:
                print("result> " + result)

if __name__ == '__main__':
    main()
