data = [
    [3, 5, 2, 4, 1], # 0번째 행
    [4, 5, 1], # 1번째 행
    [4, 4, 1, 5, 4], # 2번째 행
    [4, 5] # 3번째 행
]
 
result = {}
 #    1      [4, 5, 1]
for index, lis in enumerate(data):
    list_sum = sum(lis) # 10
    list_len = len(lis) # 3
 
    # result[0] = (15, 5)
    # result[1] = (10, 3)
    # result[2] = (18, 5)
    # result[3] = (9, 2)
    result[index] = (list_sum, list_len)
 
print(result)