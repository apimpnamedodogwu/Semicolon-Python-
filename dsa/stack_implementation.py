def make_a_stack():
    stack = []
    return stack


def empty_stack(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("Pushed item is " + item)


def pop_stack(stack):
    if empty_stack(stack) is False:
        return stack.pop()
    else:
        return f"Empty stack cannot be popped!"


stack_ = make_a_stack()
push(stack_, str(1))
push(stack_, str(2))
push(stack_, str(3))
push(stack_, str(4))
print("Popped item is " + pop_stack(stack_))
