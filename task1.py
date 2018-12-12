import time
from task2 import LinkedQueue
from task3 import quick_sort

def merge(S1, S2, S):

    while not S1. is_empty() and not S2. is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1. is_empty():
        S.enqueue(S1.dequeue())
    while not S2. is_empty():
        S.enqueue(S2.dequeue())


def merge_sort(S):

    n = len(S)
    if n < 2:
        return

    S1 = LinkedQueue()
    S2 = LinkedQueue()
    while len(S1) < n // 2:
        S1.enqueue(S.dequeue())
    while not S. is_empty():
        S2.enqueue(S.dequeue())

    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)



n = LinkedQueue()
n.enqueue(3)
n.enqueue(5)
n.enqueue(1)
n.enqueue(2)


print("Queue: ", n.print_queue())
start1 = time.process_time()
merge_sort(n)
stop1 = time.process_time()
print("Sorted queue: ", n.print_queue())

print("")


m = LinkedQueue()
m.enqueue(3)
m.enqueue(5)
m.enqueue(1)
m.enqueue(2)

print("Queue: ", m.print_queue())
start2 = time.process_time()
quick_sort(m)
stop2 = time.process_time()
print("Sorted queue: ", m.print_queue())


print(stop1-start1, stop2-start2)

