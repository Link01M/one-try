import re
fath = input("请输入文件路径：")
f = open(fath, "r", encoding="utf-8")
f.seek(0)
i = 0
num = 0
data = f.read()
m = re.findall(r"\bdo\b", data)
num += len(m)
m = re.findall(r"\belse\b", data)
num += len(m)
m = re.findall(r"\benum\b", data)
num += len(m)
m = re.findall(r"\bextern\b", data)
num += len(m)
m = re.findall(r"\bfloat\b", data)
num += len(m)
m = re.findall(r"\bfor\b", data)
num += len(m)
m = re.findall(r"\bgoto\b", data)
num += len(m)
m = re.findall(r"\bif\b", data)
num += len(m)
m = re.findall(r"\bint\b", data)
num += len(m)
m = re.findall(r"\blong\b", data)
num += len(m)
m = re.findall(r"\bregister\b", data)
num += len(m)
m = re.findall(r"\breturn\b", data)
num += len(m)
m = re.findall(r"\bshort\b", data)
num += len(m)
m = re.findall(r"\bsigned\b", data)
num += len(m)
m = re.findall(r"\bsizeof\b", data)
num += len(m)
m = re.findall(r"\bstatic\b", data)
num += len(m)
m = re.findall(r"\bstruct\b", data)
num += len(m)
m = re.findall(r"\bswitch\b", data)
num0 = len(m)
num += len(m)
m = re.findall(r"\btypedef\b", data)
num += len(m)
m = re.findall(r"\bunion\b", data)
num += len(m)
m = re.findall(r"\bunsigned\b", data)
num += len(m)
m = re.findall(r"\bvoid\b", data)
num += len(m)
m = re.findall(r"\bvolatile\b", data)
num += len(m)
m = re.findall(r"\bwhile\b", data)
num += len(m)
m = re.findall(r"\bdouble\b", data)
num += len(m)
m = re.findall(r"\bbreak\b", data)
num += len(m)
m = re.findall(r"\bcase\b", data)
num += len(m)
m = re.findall(r"\bchar\b", data)
num += len(m)
m = re.findall(r"\bconst\b", data)
num += len(m)
m = re.findall(r"\bcontinue\b", data)
num += len(m)
m = re.findall(r"\bdefault\b", data)
num += len(m)
print(num)
print(num0)
f.close()

f = open(fath, "r", encoding="utf-8")
count = len(f.readlines())
f.seek(0)
flag = 0
num = 0
num2 = 0
for i in range(count):
    data = f.readline().strip()
    m = re.findall(r"\bswitch\b", data)
    if len(m) != 0:
        flag = 1
    if flag == 1:
        m = re.findall(r"\bcase\b", data)
        if len(m) != 0:
            num += len(m)
        m = re.findall(r"\bdefault\b", data)
        if len(m) != 0:
            flag = 0
            print(num, end=" ")
            num = 0
print()
f.close()


class Stack(object):
    '''定义栈类'''
    def __init__(self):
        self.list = []
    '''判断栈空'''
    def is_empty(self):
        return self.list == []
    '''在栈顶添加元素'''
    def push(self, data):
        self.list.append(data)
    '''弹出栈顶元素'''
    def pop(self):
        return self.list.pop()
    '''取栈顶元素，不修改栈内容'''
    def peek(self):
        return self.list[-1]
    '''栈大小'''
    def size(self):
        return len(self.list)

f = open(fath, "r", encoding="utf-8")
count = len(f.readlines())
f.seek(0)
s = 0
god = [0 for i in range(10000)]
for i in range(count):
    data = f.readline().strip()
    j = 0
    while j <= len(data) - 1:
        if data[j] == "{":
            god[s] = "{"
            s += 1
        if data[j] == "}":
            god[s] = "}"
            s += 1
        if data[j] == "i":
            if j == 0 and j + 1 == len(data) - 1:
                if data[j + 1] == "f":
                    god[s] = "if"
                    s += 1
                    j = j + 1
                    continue
            if j == 0 and j + 1 < len(data) - 1:
                if data[j + 1] == "f":
                    if data[j + 2].isalpha() == False:
                        god[s] = "if"
                        s += 1
                        j = j + 1
                        continue
            if j != 0 and j + 1 == len(data) - 1 and data[j - 1] == " ":
                if data[j + 1] == "f":
                    god[s] = "if"
                    s += 1
                    j = j + 1
                    continue
            if j != 0 and j + 1 < len(data) - 1 and data[j - 1] == " ":
                if data[j + 1] == "f":
                    if data[j + 2].isalpha() == False:
                        god[s] = "if"
                        s += 1
                        j = j + 1
                        continue
        if data[j] == "e":
            q1 = 0
            q2 = 0
            if j == 0 and j + 3 == len(data) - 1:
                if data[j + 1] == "l":
                    if data[j + 2] == "s":
                        if data[j + 3] == "e":
                            god[s] = "else"
                            s += 1
                            j = j + 3
                            continue
            if j == 0 and j + 3 < len(data) - 1:
                if data[j + 1] == "l":
                    if data[j + 2] == "s":
                        if data[j + 3] == "e":
                            if data[j + 4] == " ":
                                d1 = j + 5
                                while d1 <= len(data) - 1:
                                    if q2 == 1 and data[d1].isalpha() == False:
                                        break
                                    if q2 == 1 and data[d1].isalpha() == True:
                                        q2 = 0
                                        break
                                    if q1 == 1 and data[d1] == "f":
                                        q2 = 1
                                    if q1 == 1 and data[d1] != "f":
                                        break
                                    if q1 == 0 and data[d1] == "i":
                                        q1 = 1
                                    if q1 == 0 and data[d1] != " " and data[d1] != "i":
                                        break
                                    d1 += 1
                if q2 == 0:
                    god[s] = "else"
                    s += 1
                    j = j + 3
                    continue
                if q2 == 1:
                    god[s] = "else if"
                    s += 1
                    j = j + 6
                    continue
            if j != 0 and j + 3 == len(data) - 1 and data[j - 1].isalpha() == False:
                if data[j + 1] == "l":
                    if data[j + 2] == "s":
                        if data[j + 3] == "e":
                            god[s] = "else"
                            s += 1
                            j = j + 3
                            continue
            if j != 0 and j + 3 < len(data) - 1 and data[j - 1].isalpha() == False:
                if data[j + 1] == "l":
                    if data[j + 2] == "s":
                        if data[j + 3] == "e":
                            if data[j + 4] == " ":
                                d1 = j + 5
                                while d1 <= len(data) - 1:
                                    if q2 == 1 and data[d1].isalpha() == False:
                                        break
                                    if q2 == 1 and data[d1].isalpha() == True:
                                        q2 = 0
                                        break
                                    if q1 == 1 and data[d1] == "f":
                                        q2 = 1
                                    if q1 == 1 and data[d1] != "f":
                                        break
                                    if q1 == 0 and data[d1] == "i":
                                        q1 = 1
                                    if q1 == 0 and data[d1] != " " and data[d1] != "i":
                                        break
                                    d1 += 1
                if q2 == 0:
                    god[s] = "else"
                    s += 1
                    j = j + 3
                    continue
                if q2 == 1:
                    god[s] = "else if"
                    s += 1
                    j = j + 6
                    continue
        j += 1

f.close()
stack = Stack()
str1 = "if"
str2 = "else"
str3 = "{"
str4 = "}"
str5 = "else if"
num5 = 0
num6 = 0
xun = 1
flag1 = 0
for i in range(s - 1):

    if god[i] == str5:
        stack.push(str5)
    if god[i] == str1:
        stack.push(str1)
    if god[i] == str2:
        if stack.peek() == str1:
            stack.pop()
            num5 += 1
        if stack.peek() == str5:
            while xun == 1:
                if stack.peek() == str1:
                    stack.pop()
                    num6 += 1
                    break
                else:
                    stack.pop()
    if god[i] == str3 and flag1 == 1:
        stack.push(str3)
    if god[i] == str3 and flag1 == 0:
        flag1 = 1
        stack.push(str3)

    if god[i] == str4:
        if stack.peek() == str5:
            while xun == 1:
                if stack.peek() == str1:
                    stack.pop()
                    break
                else:
                    stack.pop()
        if stack.peek() == str3:
            stack.pop()

f.close()
print(num5)
print(num6)
