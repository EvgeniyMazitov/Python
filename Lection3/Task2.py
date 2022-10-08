def sum(x, y):
    return x+y


def f(x, y): return x+y


def sum1(x, y): return x+y


def mylt(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))
    # return op a,b


calc(sum, 4, 5)
calc(f, 4, 5)
calc(sum1, 4, 5)
calc(lambda x, y: x+y, 4, 5)
