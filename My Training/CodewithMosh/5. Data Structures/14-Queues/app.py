# Queues
# imagine that module is a bucket with a bunch of reusable code

from collections import deque
import queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)
if not queue:
    print("empty")
