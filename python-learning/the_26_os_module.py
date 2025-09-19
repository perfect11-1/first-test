import os

current_dir = os.getcwd()  # 获取当前工作目录
print(current_dir)

#os.chdir('D:\\')  # 切换到指定目录
#print(os.getcwd())

files_and_dirs = os.listdir()  # 获取当前目录下的所有文件和目录
print(files_and_dirs)

os.mkdir('new_dir')  # 创建一个新目录
print(os.listdir())  # 确认新目录已被创建

os.rmdir('new_dir')  # 删除一个目录
print(os.listdir())  # 确认新目录已被删除

os.mkdir('old_name')  # 创建一个新目录
os.rename('old_name', 'new_name')  # 重命名一个文件或目录
print(os.listdir())  # 确认文件已被重命名
os.removedirs('new_name')  # 删除一个目录
print(os.listdir())  # 确认目录已被删除

home_directory = os.getenv('HOME')  # 获取用户主目录
print(home_directory)

os.system('dir')  # 运行一个系统命令

# 创建一个新文件
with open('./python-learning/new_file.txt', 'a') as f:
    f.write('\n这是一个新文件')
print(os.listdir())  # 确认文件已被创建
