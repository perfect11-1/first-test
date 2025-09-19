def test():  #无参函数
    print('这是一个函数')

test()

print('下一个样例#################################')

def is_orange(f):  #有参函数
    if f == 'orange':
        return True
    else:
        return False

bool1 = is_orange('orange')
print(bool1)

bool2 = is_orange('apple')
print(bool2)

print('下一个样例#################################')
def make_pizza(*toppings):  #将所有的参数收集到一个元组里面
    topping_str = ",".join(toppings)
    print(f'我要制作一个披萨，配料有：{topping_str}')

make_pizza('pepperoni', 'mushrooms', 'green peppers')

print('下一个样例#################################')
def make_noodles(**kwargs):  #将所有的参数收集到一个字典里面
    noodles_info = ''
    for key, value in kwargs.items():
        noodles_info += f"{key}: {value} "
    print(f"我要制作一个{noodles_info}的面条")

make_noodles(name='tomato_noodle', vegetables=['cabbage', 'mushrooms', 'green peppers'])
