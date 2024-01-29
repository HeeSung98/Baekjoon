class Stack:
    def __init__(self):
        self.item = []
        self.sp = -1
    
    def push(self, item):
        self.item.append(item)
        self.sp += 1

    def pop(self):
        if self.sp != 0:
            self.sp -= 1
            return self.item.pop()
        else:
            return "스택이 비어있습니다."
        
    def peek(self):
        return self.item[self.sp]

n = int(input())
input_list = []

for i in range(n):
    input_list.append(int(input()))

stack = Stack()
count = 0
result = ""

for i in input_list:
    if count < i:
        for j in range(count, i):
            count += 1
            stack.push(count)
            result += '+'
    if stack.peek() == i:
        stack.pop()
        result += '-'
    else:
        result = 'NO'
        break

if result != 'NO':
    for i in result:
        print(i)
else:
    print(result)