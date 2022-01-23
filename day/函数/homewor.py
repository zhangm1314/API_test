# 定义函数：(要求：定义函数处理逻辑。input输入操作在函数之外)
from re import split

sum = input("请输入数字：")
sp_sum = split(r',', sum)
print(sp_sum)


def get_num(nums):
    # 1.将用户输入的所有数字相乘之后对20取余数
    result = 1
    for num in nums:
        result *= int(num)
    return result % 20
# 2.用户输入的数字个数不确定


res = get_num(sp_sum)
print(res)