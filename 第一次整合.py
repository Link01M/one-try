import re
f = open(r"D:\1.txt", "r", encoding="utf-8")
f.seek(0)
i=0
num=0
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

f = open(r"D:\1.txt", "r", encoding="utf-8")
count = len(f.readlines())
f.seek(0)
flag = 0
num = 0
num2 = 0
for i in range(count):
    data = f.readline().strip()
    m = re.findall(r"\bswitch\b",data)
    if len(m) != 0:
        flag = 1
        continue
    if flag == 1:
        m = re.findall(r"\bcase\b", data)
        if len(m) != 0:
            num += len(m)
        m = re.findall(r"\bdefault\b", data)
        if len(m) != 0:
            flag = 0
            print(num,end=" ")
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
f = open(r"D:\1.txt","r",encoding="utf-8")
count=len(f.readlines())+1
f.seek(0)
num5=0
flag2=0
flag1=0
str1="if"
str2="else"
str3="{"
str4="}"
str5="else if"
stack=Stack()
for i in range(count):
    data1 = f.readline().strip()
    m1 = re.findall(r"\bif\b", data1)
    m2 = re.findall(r"\belse\b", data1)
    if (len(m1) != 0) and (len(m2) != 0):
        stack.push(str5)
    if (len(m1) != 0)and(len(m2) == 0):
        stack.push(str1)
    if (len(m2) != 0)and(len(m1) == 0):
        if stack.peek()==str1:
            stack.pop()
            num5 += 1
        else:
            stack.push(str2)
    result = str3 in data1
    if (result == True) and (flag1 == 1):
        stack.push(str3)
    if (result == True)and(flag1==0):
        flag1 = 1

    result = str4 in data1
    if result == True:
        if stack.peek() == str3:
            stack.pop()
        else:
            stack.push(str4)
f.close()
print(num5)
q1=0
q2=0
q3=0
num6 = 0
for i in range(10000):
    if(stack.is_empty() == True):
        break
    else:
        a = stack.pop()
        if a == str2:
            num6 += 1

print(num6)



