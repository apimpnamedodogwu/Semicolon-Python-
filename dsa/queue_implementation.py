def create_queue():
    stack = []
    return stack


def size(stack):
    return len(stack)


def enqueue(stack, item):
    stack.append(item)


def dequeue(stack):
    if len(stack) < 1:
        return
    return stack.pop(0)


queue_ = create_queue()
enqueue(queue_, str(1))
enqueue(queue_, str(2))
enqueue(queue_, str(3))
enqueue(queue_, str(4))
enqueue(queue_, str(5))
print(queue_)
print(f"Item to be popped is {dequeue(queue_)}")
