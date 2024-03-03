# Basic BFS Tutorial

## Key Concepts:

1. BFS
2. Queues

## Things Learned:

- Keep two lists
  - Queue
  - Visited
- When you pop an element off the begining of the queue ensure that it is not in visited (if this is the case:)
  - Add it to the visited list
  - Explore its neighbors and for those who have not been visited add them to the queue
- Using the deque class from the collections library
