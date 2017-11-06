def divides(x,y):
    return y != 0 and x % y == 0

def add_to_each(k,ls):
    return [[k] + l for l in ls]

def decomp(N,T):
    if T == 0:
        return []
    return [[N[i]] + rest for i in range(len(N)) for rest in decomp([N[j] for j in range(len(N)) if i != j and divides(N[j],N[i])],T/N[i])]
