
def add(a, b):
    return str(int(a) + int(b))

subLambda = lambda a, b: str(int(a) - int(b))
def sub(a, b): return subLambda(a, b)

def mul(a,b): return str(int(a) * int(b))

def div(a, b):
    return str(int(a) / int(b))
