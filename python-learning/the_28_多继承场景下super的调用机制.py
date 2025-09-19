class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

d = D()
# 输出结果
# A
# C
# B
# D
# 说明：
# 1. 调用super().__init__()方法时，会根据MRO（Method Resolution Order）来调用父类的方法。
# 2. MRO是根据类的继承关系来确定的，例如在D类中，super().__init__()会先向上调用B的__init__方法，然后向上调用C的__init__方法，最后向上调用A的__init__方法。
# 3. 所以输出时先执行A的__init__方法，然后执行C的__init__方法，最后执行B的__init__方法，最后执行D的__init__方法。