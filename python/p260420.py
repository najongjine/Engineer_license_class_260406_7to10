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

print(count_dict)

####################
k=['a','b']
c=['c','d']
a=[k,c]
print(a)

######indexing######
s="hello"
print(s[-5]) # == s[0] 이랑 같아요. python은 내림차순으로 index 첨자도 가능해요