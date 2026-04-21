"""
int a=0;
if(1){
 int a=1;
}
"""

# 파이썬은 함수, class 영역 빼고는 scope가 없습니다
a=0
if a:
    #print("true 로 판정")
    a+=1
elif a<0:
    #print("a가 0보다 작다 판정")
    --a
else:
    #print("0 으로 판정")
    a=0

for i in range(3):
    if(i%2==0):
        break
    i=i
    #print(i)

for i in [1,2]:
    i=i
    #print(i)

#########함수###########
def add(a,b):
    return a+b

#print(add(1,2)) #3

"""
python은 default 매개변수 기능이 있어서, 데이터 주고싶으면 주고, 귀찬으면 안줘도 되요
"""
def add(a="데이터",b=" 안줬잔아"):
    # 문자열 + 문자열은 문자열 이어 붙이기로 작동해요
    return a+b

"""
파이썬은 리턴으로 1개 이상의 데이터를 뱉을수 있어요
"""
def swap(a,b):
    # 변수끼리 데이터 바꿀때도 괴상한 문법으로 쉽게 데이터 바꾸기 할수 있어요
    [b,a]= [a,b]
    return a,b,3,45,6,7,8,9,896,2,545,4,
a=1
b=2
#print(swap(a,b))
#print(f"main a: {a}")
#print(f"main b: {b}")

"""
파이썬은 scope 개념이 함수하고 class 에만 있어요
"""
def change(a=1):
    a="바뀜"
    return a
a=1
change(a)
#print(a)

def change2(a):
    a[0]="바뀜"
    return a
a=[1,2]
change2(a)
print(a)



