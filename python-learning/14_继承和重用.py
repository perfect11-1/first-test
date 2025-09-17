class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        print(f'{self.name}正在吃')
    def sleep(self):
        print(f'{self.name}正在睡')
    def make_sound(self):
        print(f'{self.name}正在叫')
#继承
class Dog(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    def guard_home(self):
        print(f'{self.name}正在看家')
    def make_sound(self):  #重写父类的方法
        print(f'{self.name}正在汪汪叫')

class Cat(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    def cat_mouse(self):
        print(f'{self.name}正在抓老鼠')
    def make_sound(self):  #重写父类的方法
        print(f'{self.name}正在喵喵叫')
    
mimi = Cat('mimi', 1, '女')
mimi.make_sound()
mimi.cat_mouse()

dog = Dog('旺财', 2, '男')
dog.make_sound()
dog.guard_home()
