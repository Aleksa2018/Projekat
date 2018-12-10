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

start1 = time.clock()
merge_sort(n)
stop1 = time.clock()


start2 = time.clock()
quick_sort(n)
stop2 = time.clock()

print(stop1-start1,stop2-start2)