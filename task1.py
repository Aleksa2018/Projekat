import time
from task2 import LinkedQueue
from task3 import quick_sort
import random

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
m = LinkedQueue()
p = LinkedQueue()


for i in range(10000):
    n.enqueue(random.randint(0,1000000))


for i in range(100000):
    m.enqueue(random.randint(0,1000000))


for i in range(1000000):
    p.enqueue(random.randint(0,1000000))


print("Queue: ", n.print_queue())
start1 = time.clock()
merge_sort(n)
stop1 = time.clock()
print("Sorted queue: ", n.print_queue())
print(stop1-start1)

t1=stop1-start1


print("")


print("Queue: ", m.print_queue())
start1 = time.clock()
merge_sort(m)
stop1 = time.clock()
print("Sorted queue: ", m.print_queue())
print(stop1-start1)

t2=stop1-start1


print("")


print("Queue: ", p.print_queue())
start1 = time.clock()
merge_sort(p)
stop1 = time.clock()
print("Sorted queue: ", p.print_queue())
print(stop1-start1)

t3=stop1-start1


print("")


n1 = LinkedQueue()
m1 = LinkedQueue()
p1 = LinkedQueue()


for i in range(10000):
    n1.enqueue(random.randint(0,1000000))


for i in range(100000):
    m1.enqueue(random.randint(0,1000000))


for i in range(1000000):
    p1.enqueue(random.randint(0,1000000))


print("Queue: ", n1.print_queue())
start1 = time.clock()
quick_sort(n1)
stop1 = time.clock()
print("Sorted queue: ", n1.print_queue())
print(stop1-start1)

t11=stop1-start1


print("")


print("Queue: ", m1.print_queue())
start1 = time.clock()
quick_sort(m1)
stop1 = time.clock()
print("Sorted queue: ", m1.print_queue())
print(stop1-start1)

t22=stop1-start1


print("")


print("Queue: ", p1.print_queue())
start1 = time.clock()
quick_sort(p1)
stop1 = time.clock()
print("Sorted queue: ", p1.print_queue())
print(stop1-start1)

t33=stop1-start1

print("")

print(t1-t11,t2-t22,t3-t33)
