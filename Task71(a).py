def find_common_elements(list1, list2):
    common_elements = list(set(list1).intersection(list2))
    return common_elements

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(list1, list2)
print("The common elements are:", common_elements)