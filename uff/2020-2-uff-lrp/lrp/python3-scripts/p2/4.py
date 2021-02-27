import itertools

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

a = [2, 2, 2, 4, 6, 5, 9, 13]
sum_n = 0

for i in range(2,len(a),1):
    for t in itertools.combinations(a,i):
        v = [t[i+1]-t[i] for i in range(len(t)-1)]
        if all_equal(v) == True:
            sum_n = sum_n + 1
        
