import os

files = [file for file in os.listdir(os.getcwd())]

print(files)
print(os.curdir)
print(os.getcwd())
os.mkdir('some_dir')
os.chdir('some_dir')
print(os.getcwd())
os.chdir('..')
os.rmdir('some_dir')
print(os.getcwd())

for file in files:
    print(file,)
    print(os.path.getsize(file))

