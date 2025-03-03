class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    
s1 = Stack()
s1.pop()
'NE OK'
s1.push(1)
s1.push(2)
s1.push(25)
s1.push(21)
s1.show()
[1, 2, 25, 21]
s1.pop()
'OK'
s1.show()
[1, 2, 25]
s1.pop()
'OK'
s1.show()
[1, 2]