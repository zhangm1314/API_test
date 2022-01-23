"""
输入一个人的身高(m)和体重(kg)，根据BMI公式(体重除以身高的平方)计算他的BMI指数
a.例如：一个65公斤的人，审改是1.62m，则BMI为：65 / 1.62 **2 = 24.8
b. 根据BMI指数，给与相应提醒
低于18.5：过轻   18.5-25：正常   25-28：过重   28-32：肥胖    高于32：严重肥胖
"""
height = float(input("请输入您的身高(m)："))
weight = float(input("请输入您的体重(kg)："))


def get_bmi(heights, weights):
    num = weights / heights ** 2
    if num < 18.5:
        print('过轻')
    elif 18.5 <= num < 25:
        print('正常')
    elif 25 <= num < 28:
        print('过重')
    elif 28 <= num < 32:
        print('肥胖')
    elif 32 < num:
        print('严重肥胖')


get_bmi(height, weight)