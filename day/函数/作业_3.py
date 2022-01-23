"""
通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘【4】除 操作，选择之后返回对应操作的值
"""


def calculator(num1, num2):
    print('请选择要操作的公式')
    print('1.加')
    print('2.减')
    print('3.乘')
    print('4.除')
    if num2 == 0:
        return "被除数能为0"
    num = int(input('请输入要操作的公式：'))
    if num == 1:
        return num1 + num2
    if num == 2:
        return num1 - num2
    if num == 3:
        return num1 * num2
    if num == 4:
        return num1 / num2


res = calculator(1, 6)
print(res)
