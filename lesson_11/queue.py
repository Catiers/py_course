Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class EmptyQueueError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"EmptyQueueError: message: {self.message}"

    
raise EmptyQueueError("Очередь пустая")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    raise EmptyQueueError("Очередь пустая")
EmptyQueueError: EmptyQueueError: message: Очередь пустая
try:
    raise EmptyQueueError("Очередь пустая")
except EmptyQueueError as e:
    print(e)

    
EmptyQueueError: message: Очередь пустая
class Queue:
    def __init__(self):
        self.__queue = []
    def get(self)"
    
SyntaxError: unterminated string literal (detected at line 4)
class Queue:
    def __init__(self):
        self.__queue = []
    def get(self):
        if len(self.__queue) < 1:
            raise EmptyQueueError("Очередь пустая")
        return self.__queue.pop(0)
        
    def put(self, value):
        self.__queue.append(value)

        
q1 = Queue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(5)
q1.get()
1
q1.get()
2
q1.get()
3
q1.get()
5
q1.get()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    q1.get()
  File "<pyshell#21>", line 6, in get
    raise EmptyQueueError("Очередь пустая")
EmptyQueueError: EmptyQueueError: message: Очередь пустая
>>> class EmptyQueueError(Exception):
...     def __init__(self, message):
...         self.message = message
...     def __str__(self):
...         return f"EmptyQueueError: message: {self.message}"
... 
...     
>>> class Queue:
...     def __init__(self):
...         self.__queue = []
...     def get(self):
...         if len(self.__queue) < 1:
...             raise EmptyQueueError("Очередь пустая")
...         return self.__queue.pop(0)
...         
...     def put(self, value):
...         self.__queue.append(value)
... 
...         
>>> q1 = Queue()
>>> q1.put(1)
>>> q1.put(2)
>>> q1.put(3)
>>> q1.put(5)
>>> q1.get()
1
>>> q1.get()
2
>>> q1.get()
3
>>> q1.get()
5
>>> q1.get()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    q1.get()
  File "<pyshell#35>", line 6, in get
    raise EmptyQueueError("Очередь пустая")
EmptyQueueError: EmptyQueueError: message: Очередь пустая
