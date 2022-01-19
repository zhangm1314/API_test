# list1 = [0, 1, 2, 3, 4, 5]  # 列表解包
# print(*list1)


# def print_info(**kwargs):
#     print(kwargs)
#     for key, values in kwargs.items():
#         print(key, values)
#
#
# person_info = {'city': '深圳', '姓名': 'zhangm'}
# print_info(**person_info)


person_info = {'city': '深圳', '姓名': 'zhangm'}
for key, values in person_info.items():
    print(key, values)