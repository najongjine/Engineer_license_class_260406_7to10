set1={1,2,2,3}

# dicnationary 는 C 언의 struct이랑 비슷 하다.
dic1={'name':'John', 'age':30, 'city':'New York'}

####################

numbers = [1, 2, 3, 4, 5]
numbers[1]=1*1

result = {} # {1:1}
#   1
for num in numbers:
    # result[1]= 1*1
    result[num] = num * num

#print(result)
#######################################
text = "banana"

count_dict = {} # {'b':1, 'a':3, 'n':2}

for ch in text: # n
    if ch in count_dict: # n 가 count_dict 안에 있니
        count_dict[ch] += 1 # count_dict['n'] = count_dict['n'] + 1
    else:
        count_dict[ch] = 1 

#print(count_dict)

####################
k=['a','b']
c=['c','d']
a=[k,c]
#print(a)

######indexing######
s="hello"
#print(s[-5]) # == s[0] 이랑 같아요. python은 내림차순으로 index 첨자도 가능해요
#print(s[1:3]) # 1번째부터 3번째 전까지 출력해요. 즉 1번째랑 2번째만 출력해요.

#s[start:end:step] step =2 면 2칸씩 건너뛰면서 출력해요.
#print(s[0:5:2]) # hlo

s=[1,2,3,4,5,6,7,8,9]
#print(s[-5:-1:3]) # [5,8]
#print(s[:])

##############
s=[]
s.append(1) # 배열 끝에다가 원소를 붙인다.
s.extend([4,5]) # 배열 끝에다가 여러개의 원소를 붙인다.
s.insert(1,10) # 1번째 위치에 10을 넣는다.
#print(s)

s=[1,1,2,2,3,3,3]
s.remove(1) # 배열에서 값을 제거한다.
#pop(index) : 배열에서 인덱스에 해당하는 값을 제거한다.
#del s[index] : 배열에서 인덱스에 해당하는 값을 제거한다.
#clear() : 배열을 비운다.
#count(value) : 배열에서 값의 개수를 센다.
#index(value) : 배열에서 값의 인덱스를 찾는다.
#reverse() : 배열을 뒤집는다.
#sort() : 배열을 정렬한다.
#sorted(s) : 배열을 정렬한다.
print(s)