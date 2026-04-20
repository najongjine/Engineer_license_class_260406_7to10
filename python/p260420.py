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

count_dict = {}

for ch in text:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

print(count_dict)