from collections import deque

stack = deque()

stack.append(8)
stack.append(45)
stack.append(2)
print(stack)
stack.pop()
stack.pop()
stack.pop()
print(stack)