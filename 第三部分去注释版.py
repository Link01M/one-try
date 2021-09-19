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
fath = input("请输入文件路径：")
f = open(fath, "r", encoding="utf-8")
count = len(f.readlines())
f.seek(0)
s = 0
god = [0 for i in range(10000)]
for i in range(count):
    data = f.readline().strip()
    j = 0
    stop = 0
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
