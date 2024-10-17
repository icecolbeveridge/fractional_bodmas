import itertools
import collections
import time
start = time.time()

class Func():
    def __init__(self, fn, name):
        self.fn = fn
        self.name = name
    def __call__(self,x,y):
        return self.fn(x,y)
    def __repr__(self):
        return self.name

Fraction = collections.namedtuple("Fraction", "n d")

add = Func(lambda x,y: Fraction(x.n * y.d + x.d * y.n, y.d * x.d) , "+")
sub = Func(lambda x,y: Fraction(x.n * y.d - x.d * y.n, y.d * x.d) , "-")
mul = Func(lambda x,y: Fraction(x.n * y.n, y.d * x.d), "*")
div = Func(lambda x,y: Fraction(x.n * y.d, x.d * y.n), "/")

ops = {add, sub, mul, div}

digits = set(range(10))

def get_fractions(digits):
    if len(digits) == 0:
        return
    for p in itertools.permutations(digits, 2):
        if p[1] != 0:
            yield p


def generate_stack(stack, ops, digits):
    if len(ops) == 0: # we're done
        yield stack
        return
    for n, d in get_fractions(digits):
        ndigits = digits.difference({n,d})
        nstack = stack.copy() + [Fraction(n,d)]
        yield from generate_stack(nstack, ops, ndigits)
            
    if  len(ops) > len(digits)/2:
        for o in ops:
            nops = ops.difference({o})
            nstack = stack.copy() + [o]
            yield from generate_stack(nstack, nops, digits)

def eval_stack(stack):
    s = []
    for si in stack:
        if si in ops:
            try:
                a = s.pop()
                b = s.pop()
                s.append( si(a,b))
            except IndexError:
                print(stack, s, si)
                raise IndexError
        else:
            s.append( si )
    if len(s) != 1:
        raise ValueError
    return s[0]

def val(f):
    return f.n / f.d

def ge(f, g):
    return f.n * g.d >= f.d * g.n)

mx = Fraction(0,1)
n = 0
for s in generate_stack([], ops, digits):
    try:
        v = eval_stack(s)
        if ge(v, mx):
            mx = v 
            print (v, val(v), s)
    except ZeroDivisionError:
        pass
    n += 1
    if n % 10_000_000 == 0:
        t = time.time() - start
        e = t / n * 609638400
        print(f"{n:,} in {t}/{e}")
print(n)
