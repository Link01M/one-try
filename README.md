# 编码规范
## 缩进
- 从属关系的表示：如果B从属于A, 那么B的开头，就跟A的开头保持距离L(比如说1个TAB的距离或者4个空格的距离)
- 统一的缩进风格：如果C从属于B, 那么C的开头，就跟B的开头同样保持距离L(比如说1个TAB的距离或者4个空格的距离)。那么自然的，B就跟A的开头就会保持距离2 * L(即2个TAB或者8个空格的距离)
- 一般情况下等号(包括if判断语句里的==)两边都要有一个空格(除了end=""的情况)
```
if A == 1：
   if B == 1:
       if C == 1:
```
```
a = 1
print(a,end="")
```
## 变量命名
- 变量命名用可表达具体意思的单词前后缀组合而成
- 变量命名用可表达具体意思的单词前后缀还有下划线组合而成
- 变量命名可以在后面加数字来表示不同
```
key_word
keyword
flag1 flag2 flag3
```
## 每行最多字符数
- 不超过100个字符数(不包括注释)
## 函数最大行数
- 不超过100行
## 函数、类命名
- 使用函数的具体作用来命名,首字母大写
```
def Ruzhan()  # 入栈
def Xuncan()  # 寻参
```
## 常量
- 尽量符合该变量用途的名字，并在后面标识其作用
```
num1   # xx的个数
num2   # xx的个数
flag1  # 控制······的判断变量
grade  # 等级
```
## 空行规则
- 如果为了更容易区分代码之间的作用，避免混淆，可以在两行代码间加入空行
##注释规则
- 在变量下注释其意义和作用
- 在即将进行的步骤上标注该步骤以用来区分不同代码的作用
- 如果前面有代码并且使用#来注释时，需要在左边空两格，在右边空一格再打注释，前面没有代码就顶格，并且在右边空一格
```
num = 2  # xx的个数
flag = 2  # 用来判断是否执行xx的，如果flag等于某数就执行，不等于就不执行
# 接下是对参数的入栈
······
```
## 操作符前后空格
- 运算符前后加1个空格