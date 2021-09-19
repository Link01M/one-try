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


if __name__ == '__main__':
    stack = Stack()
    print('栈是否为空：',stack.is_empty())
    stack.push("ad")
    stack.push("bd")
    stack.push(10)
    print('栈大小：',stack.size())
    print('peek取栈顶元素：',stack.peek())
    print('---出栈---')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())