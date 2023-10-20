def multiply_lists(list1,list2):
    multiplied_list = [x*y for x, y in zip(list1,list2)]
    return multiplied_list
#example
list1 = [1,2,3]
list2 = [4,5,6]
result = multiply_lists(list1, list2)
print("the multiplied list is:", result)