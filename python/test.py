def f(a):
    m = [[x] for x in a] #[[1],[2],[3],[4]]
    b = m[:] #[[1],[2],[3],[4]]
    for i in range(len(b) - 1):
        b[i+1] += b[i]
    return sum(len(x) for x in m)
 
#print(f([1, 2, 3, 4]))