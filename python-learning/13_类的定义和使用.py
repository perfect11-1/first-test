#第一个类
class Student:
    def __init__(self, name, grade, student_id):
        self.name = name
        self.grade = grade
        self.student_id = student_id
    def study(self, subject):
        print(f'{self.name}正在学习{subject}')

    def take_exam(self, subject):
        print(f'{self.name}正在考试{subject}')

    def join_club(self, club):
        print(f'{self.name}加入了{club}')

stu1 = Student('小红', 1, 1001)
stu1.study('数学')
stu1.take_exam('数学')
stu1.join_club('足球俱乐部')

print("下一个样例#####################################")
#第二个类
class Employee:
    def __init__(self, name, employee_id, position, salary):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
    def work(self):
        print(f'{self.name}总是在努力工作')
    def promote(self, new_position):
        self.position = new_position
        print(f'{self.name}的职位变更为{self.position}')
    def raise_salary(self, amount):
        old_salary = self.salary
        self.salary += amount
        print(f'{self.name}的薪资提高到{self.salary}，之前的薪资是{old_salary}')

emp1 = Employee('张三', 1001, '讲师', 5000)
emp1.work()
emp1.promote('副教授')
emp1.raise_salary(1000)


