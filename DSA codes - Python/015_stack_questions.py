from collections import deque

def reverse_string(text):

    stack = deque()
    rstr = ''

    for i in text:
        stack.append(i)
    
    while len(stack)!=0:
        rstr += stack.pop()
    
    return rstr

print(reverse_string("We will conquere COVID-19"))
    
