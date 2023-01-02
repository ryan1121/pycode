
# 密码生成器

# 导包
import random   # 导入随机模块
import string   # 导入字符模块


# input --> 输入函数，可以提供用户输入框，然后程序接收用户的输入结果
# int --> 将用户的输入结果转换为 整型 数据
# num_pass --> 用来保存用户输入结果的 变量名称
num_pass = int(input("请输入想要生成的密码数量 : "))

# string.ascii_lowercase --> 26个小写字母
# string.ascii_uppercase --> 26个大写字母
# alp_list --> 用来保存 52个大小写字母的 变量名称
alp_list = string.ascii_lowercase + string.ascii_uppercase

# 自定义的符号变量
symbol_list = '!@#$%^&*_.'

# 密码定义 变量
password = ''

while True :    # 死循环
    if len(password) >= num_pass :  # 当密码长度符合 规定密码长度
        print(f'您的密码是 {password}') # 打印最终密码

        break   # 退出死循环

    # 定义用来保存随机数据的 列表
    rand_datalist = []

    # 生成随机数字
    random_num = random.randint(0, 9)
    # 从字母列表中随机抽取一个结果
    alp = random.choices(alp_list)[0]
    # 从符号列表中随机抽取一个结果
    symbol = random.choices(symbol_list)[0]

    # 往 随机数据列表 存放三个随机抽取出来的数据
    rand_datalist.append(random_num)
    rand_datalist.append(alp)
    rand_datalist.append(symbol)

    # for循环遍历三次，生成密码
    for i in range(3):
        if len(password) < num_pass :   # 判断已经生成的密码长度是否 小于 规定密码长度
            password += str(random.choices(rand_datalist)[0])   # 再随机从 随机数据列表中 抽取数据，并且添加进入密码字符中
        else :  # 否则
            break   # 退出循环
    
    # 完成，让我们运行试试
    