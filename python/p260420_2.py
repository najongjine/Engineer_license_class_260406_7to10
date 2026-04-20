"""
int a=0;
if(1){
 int a=1;
}
"""

# 파이썬은 함수, class 영역 빼고는 scope가 없습니다
a=0
if(False):
    a=1
print(a)