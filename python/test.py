lst = [1,2,3] # [99,2,3]
"""
dst={
1:2
2:7
3:6
}
"""
dst = {i : i* 2 for i in lst}
# s={2,4,6,99}
s = set(dst.values())
lst[0] = 99 
dst[2]=7
s.add(99)
"""
{2,4,6,99} & {2,4,7} -> len({2,4}) = 2
"""
print(len(s & set(dst.values())))