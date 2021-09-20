import time
import re
fath = input("请输入文件路径：")
level = input("请输入等级： ")
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
                    d = j + 2
                    while d < len(data1):
                        data1[d] = "1"
                        d += 1
                if data1[j + 1] == "*":
                    stop = 2
                    d1 = j + 2
                    while d1 < len(data1) - 1:
                        if d1 + 1 <= len(data1) - 1 and data1[d1] == "*" and data1[d1 + 1] == "/":
                            stop = 0
                            d = j + 2
                            while d < d1 + 1:
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
    data2 = "".join(data1)  # 对原来的字符串更新，即字符数组重新组成字符串替换掉原来的数组
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
f.close()

f = open(fath, "r", encoding="utf-8")  # 再次打开文件
count = len(f.readlines())  # 获取行数
f.seek(0)  # 读行指针回到第一行
flag = 0  # 遇到switch结构的标识
jicun = 0  # 还未放入数组用来存放case数
caseshu = [0 for i in range(1000)]  # 存放case数量的数组
shu = 0  # 存放case数组的下标
for i in range(count):
    data2 = f.readline().strip()
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
                    d = j + 2
                    while d < len(data1):
                        data1[d] = "1"
                        d += 1
                if data1[j + 1] == "*":
                    stop = 2
                    d1 = j + 2
                    while d1 < len(data1) - 1:
                        if d1 + 1 <= len(data1) - 1 and data1[d1] == "*" and data1[d1 + 1] == "/":
                            stop = 0
                            d = j + 2
                            while d < d1 + 1:
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
    data2 = "".join(data1)  # 对原来的字符串更新，即字符数组重新组成字符串替换掉原来的数组


    m = re.findall(r"\bswitch\b", data2)
    if len(m) != 0 and flag == 1:  # switch结构，刚刚开始计数case数
        flag = 2
    if len(m) != 0 and flag == 0:  # 上个switch的case数还未输出，遇到了下一个switch
        flag = 1
    if flag == 1:
        m = re.findall(r"\bcase\b", data2)
        if len(m) != 0:  # 遇到case，case数加一
            jicun += len(m)
        m = re.findall(r"\bdefault\b", data2)
        if len(m) != 0:  # 遇到default，说明要退出switch结构，输出case数
            flag = 0
            caseshu[shu] = jicun
            shu += 1
            jicun = 0
    if flag == 2:  # 这时候遇到了下一个switch，记录上一个switch结构的case数
        flag = 1
        caseshu[shu] = jicun
        shu += 1
        jicun = 0
    if i == count - 1 and num != 0:  # 最后一个switch结构没有default，当读到最后一行的时候记录case数
        caseshu[shu] = jicun
        shu += 1
nums = shu
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
s = 0  # 存进的字符串的下标数
stop = 0  # 用来判断是否是注释里的单词
god = [0 for i in range(10000)]  # 用来存放正确格式的 {，}，if，else，else if
for i in range(count):
    data = f.readline().strip()
    j = 0
    while j <= len(data) - 1:
        # 接下就是一个单词一个单词的读，先判断是否是注释里的单词，再根据i e来开始判断是否为 if ，else 或 else if
        if stop == 0 and data[j] == "/":
            if j + 1 == len(data) - 1:
                if data[j + 1] == "/":
                    break
                if data[j + 1] == "*":
                    stop = 2
                    break
            if j + 1 < len(data) - 1:
                if data[j + 1] == "/":
                    break
                if data[j + 1] == "*":
                    stop = 2
                    d1 = j + 2
                    while d1 < len(data) - 1:
                        if d1 + 1 <= len(data) - 1 and data[d1] == "*" and data[d1 + 1] == "/":
                            stop = 0
                            j = d1 + 1
                        d1 += 1
        if stop == 2 and j + 1 <= len(data) - 1:
            if data[j] == "*" and data[j + 1] == "/":
                stop = 0
        if stop == 0 and data[j] == "{":
            god[s] = "{"  # 存入{
            s += 1
        if stop == 0 and data[j] == "}":
            god[s] = "}"  # 存入}
            s += 1
        if stop == 0 and data[j] == "i":
            if j == 0 and j + 1 == len(data) - 1:
                if data[j + 1] == "f":
                    god[s] = "if"  # 存入if
                    s += 1
                    j = j + 1
                    continue
            if j == 0 and j + 1 < len(data) - 1:
                if data[j + 1] == "f":
                    if data[j + 2].isalpha() == False:
                        god[s] = "if"  # 存入if
                        s += 1
                        j = j + 1
                        continue
            if j != 0 and j + 1 == len(data) - 1 and data[j - 1] == " ":
                if data[j + 1] == "f":
                    god[s] = "if"  # 存入if
                    s += 1
                    j = j + 1
                    continue
            if j != 0 and j + 1 < len(data) - 1 and data[j - 1] == " ":
                if data[j + 1] == "f":
                    if data[j + 2].isalpha() == False:
                        god[s] = "if"  # 存入if
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
                            god[s] = "else"  # 存入else
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
                    god[s] = "else"  # 存入else
                    s += 1
                    j = j + 3
                    continue
                if q2 == 1:
                    god[s] = "else if"  # 存入else if
                    s += 1
                    j = j + 6
                    continue
            if j != 0 and j + 3 == len(data) - 1 and data[j - 1].isalpha() == False:
                if data[j + 1] == "l":
                    if data[j + 2] == "s":
                        if data[j + 3] == "e":
                            god[s] = "else"  # 存入else
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
                    god[s] = "else"  # 存入else
                    s += 1
                    j = j + 3
                    continue
                if q2 == 1:
                    god[s] = "else if"  # 存入 else if
                    s += 1
                    j = j + 6
                    continue
        j += 1
stack = Stack()
str1 = "if"
str2 = "else"
str3 = "{"
str4 = "}"
str5 = "else if"
num5 = 0  # 记录if else 结构数
num6 = 0  # 记录if-elseif-else结构数
xun = 1
for i in range(s - 1):
    if god[i] == str5:  # 遇到else if直接入栈
        stack.push(str5)
    if god[i] == str1:  # 遇到if直接入栈
        stack.push(str1)
    if god[i] == str2:  # 遇到else要判断栈顶是if 还是 else if
        if stack.peek() == str1:  # 如果栈顶是if，那么if else结果数加1
            stack.pop()  # if出栈
            num5 += 1
        if stack.peek() == str5:  # 如果是else if，那么if-elseif-else结构数加1
            while xun == 1:  # 因为是if-elseif-else结构，所以要持续出栈到最前面的if也出栈
                if stack.peek() == str1:
                    stack.pop()
                    num6 += 1
                    break
                else:
                    stack.pop()
    if god[i] == str3:
        stack.push(str3)  # 入栈{

    if god[i] == str4:
        if stack.peek() == str5:  # 如果栈顶是elseif 说明是if-elseif结果，所以持续出栈到if也出栈
            while xun == 1:
                if stack.peek() == str1:
                    stack.pop()
                    break
                else:
                    stack.pop()
        if stack.peek() == str3:  # 如果栈顶是{，则将{出栈，}也不入栈
            stack.pop()

out = int(level)  # 等级
if out == 1:
    print("total num: ", end="")
    print(num)  # 输出关键字个数
if out == 2:
    print("total num: ", end="")
    print(num)  # 输出关键字个数
    print("switch num: ", end="")
    print(nums)  # 输出switch的个数
    print("case num: ", end="")
    for i in range(shu):
        print(caseshu[i],end=" ")  # 输出每个switch结构的case数
if out == 3:
    print("total num: ", end="")
    print(num)  # 输出关键字个数
    print("switch num: ", end="")
    print(nums)  # 输出switch的个数
    print("case num: ", end="")
    for i in range(shu):
        print(caseshu[i],end=" ")  # 输出每个switch结构的case数
    print()  # 换行
    print("if-else num: ", end="")
    print(num5)  # 输出if-else结构数
if out == 4:
    print("total num: ", end="")
    print(num)  # 输出关键字个数
    print("switch num: ", end="")
    print(nums)  # 输出switch的个数
    print("case num: ", end="")
    for i in range(shu-1):
        print(caseshu[i],end=" ")  # 输出每个switch结构的case数
    print()  # 换行
    print("if-else num: ", end="")
    print(num5)  # 输出if-else结构数
    print("if-elseif-else num: ", end="")
    print(num6)  # 输出 if-elseif-else结构数
f.close()