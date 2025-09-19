#类的私有属性和私有方法只能在类内部访问，不能在类外部访问
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  #私有属性，只能在类内部访问，不能在类外部访问
       
    def get_name(self):
        return self.name
        
    def __get_age(self):     #私有方法，只能在类内部访问，不能在类外部访问
        print(f'{self.name}的年龄是{self.__age}')

    def get_age(self):
        self.__get_age()

p = Person('张三', 20)

print(p.get_name())
p.get_age()

try:
    print(p.__age)
except Exception as e:
    print(f'报错信息：{e}')
    print("不能在类外部访问私有属性")

try:
    print(p.__get_age())
except Exception as e:
    print(f'报错信息：{e}') 
    print("不能在类外部访问私有方法")

