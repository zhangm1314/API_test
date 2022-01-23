# 定义一个函数 def remove_element(e_list):
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
def remove_element(e_list):
    list1 = []
    for num in e_list:
        if num not in list1:
            list1.append(num)
    return list1


list2 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
lit = remove_element(list2)
print(lit)