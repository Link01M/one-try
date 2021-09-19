import re
fath = input("请输入文件路径：")
f = open(fath, "r", encoding="utf-8")  # 打开文件
count = len(f.readlines())  # 获取文件的行数
stop = 0  # 为实现无视注释而准备的变量条件
f.seek(0)  # 由于获取文件的行数已经让读取指针到了最后一行，需要重新回到第一行
num = 0  # 用来记录关键字的个数
nums = 0  # 用来记录switch的个数
for i in range(count):  # 一行一行的循环
    data2 = f.readline().strip()  # 把一整行除了最后面的换行符变成一个字符串
    data1 = list(data2)  # 使字符串存入一个新的字符数组，每个字符占一个空间
    j = 0  # 要对字符数组进行遍历，即实现一个一个字符的读
    while j <= len(data1) - 1:  # 13-52行 是将注释里的有可能出现的假关键字变成1，使其对关键字统计不造成影响
        if stop == 0 and data1[j] == "/":
            if j + 1 == len(data1) - 1:
                if data1[j + 1] == "/":
                    break
                if data1[j + 1] == "*":
                    stop = 2
                    break
            if j + 1 < len(data1) - 1:
                if data1[j + 1] == "/":
                    d = j+2
                    while d < len(data1):
                        data1[d] = "1"
                        d += 1
                if data1[j + 1] == "*":
                    stop = 2
                    d1 = j + 2
                    while d1 < len(data1) - 1:
                        if d1 + 1 <= len(data1) - 1 and data1[d1] == "*" and data1[d1 + 1] == "/":
                            stop = 0
                            d = j+2
                            while d < d1 + 1 :
                                data1[d] = "1"
                                d += 1
                            j = d1 + 1
                            break
                        d1 += 1
        if stop == 2 and j + 1 <= len(data1) - 1:
            if data1[j] == "*" and data1[j + 1] == "/":
                stop = 0
                d = 0
                while d < j:
                    data1[d] = "1"
                    d += 1
        if stop == 2:
            d = 0
            while d < len(data1):
                data1[d] = "1"
                d += 1
        j += 1
    data2="".join(data1)  # 对原来的字符串更新，即字符数组重新组成字符串替换掉原来的数组
    # 不直接进行修改字符串的原因是python不能对字符串进行修改
    # 接下来是利用正则表达式来寻找关键字
    m = re.findall(r"\bdo\b", data2)
    num += len(m)
    m = re.findall(r"\belse\b", data2)
    num += len(m)
    m = re.findall(r"\benum\b", data2)
    num += len(m)
    m = re.findall(r"\bextern\b", data2)
    num += len(m)
    m = re.findall(r"\bfloat\b", data2)
    num += len(m)
    m = re.findall(r"\bfor\b", data2)
    num += len(m)
    m = re.findall(r"\bgoto\b", data2)
    num += len(m)
    m = re.findall(r"\bif\b", data2)
    num += len(m)
    m = re.findall(r"\bint\b", data2)
    num += len(m)
    m = re.findall(r"\blong\b", data2)
    num += len(m)
    m = re.findall(r"\bregister\b", data2)
    num += len(m)
    m = re.findall(r"\breturn\b", data2)
    num += len(m)
    m = re.findall(r"\bshort\b", data2)
    num += len(m)
    m = re.findall(r"\bsigned\b", data2)
    num += len(m)
    m = re.findall(r"\bsizeof\b", data2)
    num += len(m)
    m = re.findall(r"\bstatic\b", data2)
    num += len(m)
    m = re.findall(r"\bstruct\b", data2)
    num += len(m)
    m = re.findall(r"\bswitch\b", data2)
    nums += len(m)
    num += len(m)
    m = re.findall(r"\btypedef\b", data2)
    num += len(m)
    m = re.findall(r"\bunion\b", data2)
    num += len(m)
    m = re.findall(r"\bunsigned\b", data2)
    num += len(m)
    m = re.findall(r"\bvoid\b", data2)
    num += len(m)
    m = re.findall(r"\bvolatile\b", data2)
    num += len(m)
    m = re.findall(r"\bwhile\b", data2)
    num += len(m)
    m = re.findall(r"\bdouble\b", data2)
    num += len(m)
    m = re.findall(r"\bbreak\b", data2)
    num += len(m)
    m = re.findall(r"\bcase\b", data2)
    num += len(m)
    m = re.findall(r"\bchar\b", data2)
    num += len(m)
    m = re.findall(r"\bconst\b", data2)
    num += len(m)
    m = re.findall(r"\bcontinue\b", data2)
    num += len(m)
    m = re.findall(r"\bdefault\b", data2)
    num += len(m)
print("total num: ", end="")
print(num)  # 输出关键字个数
f.close()
print("switch num: ", end="")
print(nums)  # 输出switch的个数

f = open(fath, "r", encoding="utf-8")  # 再次打开文件
count = len(f.readlines())  # 获取行数
f.seek(0)  # 读行指针回到第一行
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
stop = 0
god = [0 for i in range(10000)]
for i in range(count):
    data = f.readline().strip()
    j = 0
    while j <= len(data) - 1:

        if stop == 0 and data[j] == "/":
            if j + 1 == len(data) - 1:
                if data[j+1] == "/":
                    break
                if data[j+1] == "*":
                    stop = 2
                    break
            if j + 1 < len(data) - 1:
                if data[j+1] == "/":
                    break
                if data[j+1] == "*":
                    stop = 2
                    d1 = j + 2
                    while d1 < len(data) - 1:
                        if d1+1 <=len(data)-1 and data[d1] == "*" and data[d1+1] == "/":
                            stop = 0
                            j = d1+1
                        d1 += 1
        if stop == 2 and j+1 <= len(data) - 1:
            if data[j] == "*" and data[j+1] == "/":
                stop = 0
        if stop == 0 and data[j] == "{":
            god[s] = "{"
            s += 1
        if stop == 0 and data[j] == "}":
            god[s] = "}"
            s += 1
        if stop == 0 and data[j] == "i":
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
        if stop == 0 and data[j] == "e":
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

