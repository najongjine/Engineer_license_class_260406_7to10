"""
x= "abdcabcabca"  . 11
y= "ca"
"""
def fnCalculation(x,y):
    result = 0; # 1
    for i in range(len(x)): # 0 ~ 10, 2
     #      x[2:2+2]= dc
     temp = x[i:i+len(y)] 
     if temp == y: # dc == ab
       result += 1;
    return result
 
a = "abdcabcabca"
p1 = "ab";
p2 = "ca";
#               ab3ca3
out = f"ab{fnCalculation(a,p1)}ca{fnCalculation(a,p2)}"
print(out)
