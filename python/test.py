def func(lst):
    #               6//2 == 3 -> 0,1,2
    for i in range(len(lst) //2):
        """
        lst[1], lst[2] = lst[2], lst[1]
        """
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
# [6,5,4,3,2,1] 
lst = [1,2,3,4,5,6] 
func(lst)
#          12      -        9
print(sum(lst[::2]) - sum(lst[1::2]))