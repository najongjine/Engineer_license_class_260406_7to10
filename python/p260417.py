a=(1)
b=2.1
str1="ss"
str2="ss"
b1=True
set1={'A', 'B', 'C','C','C'} # 세트는 중복이 없다
set_list = list(set(set1)) # 세트를 리스트로 변환
tuple1=(1,2) # 한번 만들면, 원소값을 바꿀수 없다
tuple1=(2,3,54,65,5,3,3,4,4)
dict1={'name':'John', 'age':30, 'city':'New York'}

arr1=[1,1,2,3,4,5]
arr1_set = set(arr1) # 리스트를 세트로 변환
print(f"{arr1_set}")


"""
세트 연산 예제들
"""
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
# {1, 2, 3, 4, 5}
print(a & b)
# {3}
print(a - b)
# {1, 2}