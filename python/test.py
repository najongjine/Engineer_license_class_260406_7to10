def func(value): # 100.0
    if type(value) == type(100):
        return 100
    elif type(value) == type(""):
        return len(value) 
    else:
        return 20
 
 
a = '100.0'
b = 100.0
c = (100, 200)
#       5         20       20
print(func(a) + func(b) + func(c))
