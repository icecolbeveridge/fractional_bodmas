import itertools
import collections
n = range(1,10)

def add_frac(a, b):
    ta, ba = a 
    tb, bb = b 
    return (ta*bb + ba*tb), ba*bb

mx = 0
out = collections.defaultdict(list)
for perm in itertools.permutations(n, 8):
    # two "real patterns": multiply three together and add/sub what's left
    # or multiply two pairs together and add/sub what's left.

    a,b,c,d,e,f,g,h = perm

    # pattern 1
    top = a * c * e
    bottom = b * d * f 

    # adding f/g and sub 0 is always better than vice versa

    top, bottom = add_frac((top, bottom), (g, h))
    result = top / bottom
    out[result].append(perm)
    if result > mx:
        mx = result
        print (result, top,bottom, perm, "1")
    # pattern 2
    f1 = (a*c, b*d)
    f2 = (e*g, f*h)
    top, bottom = add_frac(f1,f2)

    result = top / bottom
    out[result].append(perm)

    if result > mx:
        mx = result
        print( result, top,bottom, perm, "2")


