import functools
import operator

ALL = int(("1" * 32), base=2)

cards =  [16+8+4+1] + ([ALL] * 4) + [8, 4, 1]


def hamming(i: int) -> int:
    return bin(i).count("1")


def or_accumulate(r) -> int:
    return functools.reduce(operator.or_, r, 0)


def proven_unsolvable(r) -> bool:
    return len(r) > hamming(or_accumulate(r))


def bitmap_to_bits(b):    
    s =[]
    i = 1
    while (b > 0):
        if b & i:
            b &=~ i
            s.append(i)        
        i = i << 1 
    return s

res = []

def solvable(a) -> bool:
    if proven_unsolvable(a):
        return False
    
    if len(a) == 1 and a[0] != 0:
        res.append(a[0])
        return True

    options = bitmap_to_bits(a[0])
    for o in options:
        r = list(map(lambda k: k &~ o, a[1:]))

        if (solvable(r)):
            res.append(o)
            return True
    
    return False
    

res = []
print(f"{cards} {solvable(cards)} {res[::-1]}")    

    
