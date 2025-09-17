from pydoc import doc
import random  
print(dir(random)) #列出模块的所有方法
print(doc(random.randint)) #给出模块某个方法的详细说明  
print(random.randint(1,10)) #随机生成一个1到10之间的整数