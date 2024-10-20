# Задача: Напишите программу, которая считывает текст из файла и
# подсчитывает количество слов в нем с помощью генератора.

def foo(filename):
    with open(filename, "r") as file:
        for line in file:
            for w in line.split(" "):
                yield w
c=0
for obj in foo("test.txt"):
    c+=1
print("task 1", c)

# Задача: Напишите функцию, которая считывает строки из файла и возвращает генератор,
# который выдает только строки, длина которых больше заданного числа.

def bar(filename, n):
    with open(filename, "r") as file:
        for line in file:
            if len(line) > n:
                yield line

for obj in bar("test.txt", 5):
    print("task 2", obj)

# Задача: Напишите программу, которая считывает строки из файла,
# преобразует их в верхний регистр и записывает в новый файл с помощью генератора.

def too(filename):
    with open(filename, "r") as file:
        for line in file:
            line = line.upper()
            yield line

with open("up.txt", "w") as up:
    for obj in too("test.txt"):
        up.write(obj)

# Задача: Напишите программу, которая считывает строки из файла и возвращает генератор,
# который выдает строки, содержащие заданное слово.

def boo(filename, w):
    with open(filename, "r") as file:
        for line in file:
            if w in line:
                yield line

for obj in boo("test.txt", "слов"):
    print("task 4",obj)

# Сортировка строк файла по алфавиту.

def hii(filename):
    with open(filename, "r") as file:
        l = sorted([line for line in file])
        for i in l:
            yield i

with open("abc.txt", "w") as file:
    for obj in hii("acb.txt"):
        file.write(obj)

# Замена всех пробелов в строках на другой символ.
def bee(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line

with open("new_test.txt", "w", encoding="utf-8") as nf:
    for line in bee("test.txt"):
        line = line.replace(" ", "H")
        nf.write(line)

# Фильтрация строк, начинающихся с определенного символа.
def faa(filename, s):
    with open(filename, "r") as file:
        for line in file:
            if line[0] == s:
                yield line
for obj in faa("test.txt", "п"):
    print(obj)



