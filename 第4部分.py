import re


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


f = open(r"D:\1.txt", "r", encoding="utf-8")
count = len(f.readlines()) + 1
f.seek(0)
num5 = 0
num6 = 0
flag2 = 0
flag1 = 0
str1 = "if"
str2 = "else"
str3 = "{"
str4 = "}"
str5 = "else if"
stack = Stack()
xun = 1
for i in range(count):
    data1 = f.readline().strip()
    m1 = re.findall(r"\bif\b", data1)
    m2 = re.findall(r"\belse\b", data1)
    if (len(m1) != 0) and (len(m2) != 0):
        stack.push(str5)
    if (len(m1) != 0) and (len(m2) == 0):
        stack.push(str1)
    if (len(m2) != 0) and (len(m1) == 0):
        if stack.peek() == str1:
            stack.pop()
            num5 += 1
        if stack.peek() == str5:
            while xun == 1:
                if (stack.peek() == str1):
                    stack.pop()
                    num6 += 1
                    break
                else:
                    stack.pop()
    result = str3 in data1
    if (result == True) and (flag1 == 1):
        stack.push(str3)
    if (result == True) and (flag1 == 0):
        flag1 = 1
        stack.push(str3)

    result = str4 in data1
    if result == True:
        if stack.peek() == str5:
            while xun == 1:
                if (stack.peek() == str1):
                    stack.pop()
                    break
                else:
                    stack.pop()
        if stack.peek() == str3:
            stack.pop()

f.close()
print(num5)
print(num6)
