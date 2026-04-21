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

print(add())

