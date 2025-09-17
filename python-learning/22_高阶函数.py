def calculate_and_print(num,calculator,formatter): #高阶函数，将函数作为参数传递给另一个函数
    result = calculator(num)
    formatter(num, result)

def print_with_vertical_line(num, result): #打印结果
    print(f"""
    | 数字参数 | {num} |
    | 计算结果 | {result} |""")

def calculate_square(num): #计算平方
    return num * num
calculate_and_print(10,calculate_square,print_with_vertical_line)

def calculate_cube(num): #计算立方
    return num * num * num
calculate_and_print(10,calculate_cube,print_with_vertical_line)

def calculate_square_root(num): #计算平方根
    return num ** 0.5
calculate_and_print(9,calculate_square_root,print_with_vertical_line)

#使用lambda匿名函数,适用于该函数只使用一次，就无需给他起名字的情况
calculate_and_print(10,lambda x: x * 5,print_with_vertical_line) 









