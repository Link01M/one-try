import re
f = open(r"D:\1.txt","r",encoding="utf-8")
f.seek(0)
i=0
num=0
li=['do','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedf','union','unsigned','void','volatile','while','auto','break','case','char','const','continue','default','double']
xun = len(li)-1
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
f.close()