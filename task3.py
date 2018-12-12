from task2 import LinkedQueue

def quick_sort(S):

    n=len(S)
    if n<2:
        return
    p=S.first()
    L=LinkedQueue()
    E=LinkedQueue()
    G=LinkedQueue()

    while not S.is_empty():
        if S.first()< p:
            L.enqueue(S.dequeue())
        elif S.first() > p:
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    quick_sort(L)
    quick_sort(G)
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())
