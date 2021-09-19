import re
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
            print(num)
            num = 0
f.close()
