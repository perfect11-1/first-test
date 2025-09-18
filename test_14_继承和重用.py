import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'python-learning'))

# 使用importlib来导入以数字开头的模块
import importlib.util
spec = importlib.util.spec_from_file_location("inheritance_module", "python-learning/14_继承和重用.py")
inheritance_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inheritance_module)
Animal = inheritance_module.Animal
Dog = inheritance_module.Dog
Cat = inheritance_module.Cat

class TestAnimalInheritance(unittest.TestCase):
    
    def test_animal_creation(self):
        """测试Animal基类的创建"""
        animal = Animal("Test", 3, "男")
        self.assertEqual(animal.name, "Test")
        self.assertEqual(animal.age, 3)
        self.assertEqual(animal.sex, "男")
    
    def test_dog_inheritance(self):
        """测试Dog类继承"""
        dog = Dog("旺财", 2, "男")
        self.assertEqual(dog.name, "旺财")
        self.assertEqual(dog.age, 2)
        self.assertEqual(dog.sex, "男")
    
    def test_cat_inheritance(self):
        """测试Cat类继承"""
        cat = Cat("mimi", 1, "女")
        self.assertEqual(cat.name, "mimi")
        self.assertEqual(cat.age, 1)
        self.assertEqual(cat.sex, "女")
    
    def test_methods_exist(self):
        """测试方法是否存在"""
        dog = Dog("Test", 1, "男")
        cat = Cat("Test", 1, "女")
        
        # 测试方法是否可调用
        self.assertTrue(callable(dog.eat))
        self.assertTrue(callable(dog.sleep))
        self.assertTrue(callable(dog.make_sound))
        self.assertTrue(callable(dog.guard_home))
        
        self.assertTrue(callable(cat.eat))
        self.assertTrue(callable(cat.sleep))
        self.assertTrue(callable(cat.make_sound))
        self.assertTrue(callable(cat.cat_mouse))
        
        # 测试方法重写
        self.assertEqual(dog.make_sound.__func__, Dog.make_sound)
        self.assertEqual(cat.make_sound.__func__, Cat.make_sound)
        self.assertNotEqual(dog.make_sound.__func__, Animal.make_sound)
        self.assertNotEqual(cat.make_sound.__func__, Animal.make_sound)

if __name__ == '__main__':
    unittest.main()