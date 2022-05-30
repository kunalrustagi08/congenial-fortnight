from collections import deque
from typing import Text

match = {'}':'{', ']':'[', ')':'('}

def check_linting(text):
    stack = deque()

    for i in text:

        if i in ['{', '(', '[']:
            stack.append(i)

        elif i in ['}', ')', ']']:

            popped_element = stack.pop() if stack else None

            if popped_element is None:
                return 'No opening brace present'

            elif popped_element != match[i]:
                return 'Mismatch, no pair formed'
    
    if stack:
        return 'No closing brace present'
    
    return True

text = "var x = { y: [1, 2, 3"
print(check_linting(text))



