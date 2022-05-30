from collections import deque

queue = deque()

queue.append(1)
queue.append(3)
queue.append(10)
queue.append(-1)
print(queue)
queue.popleft()
queue.popleft()
print(queue)