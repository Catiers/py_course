class BadPriorityError(Exception):
    """Класс для обработки ошибок неверно введённого приоритета."""

    def __init__(self, priority, message):
        self.priority = priority
        self.message = message

    def __str__(self):
        return f"BadPriorityError: priority: {self.priority}, message: {self.message}"
    

class BadIdError(Exception):
    """Класс для обработки ошибок неверно введённого индекса."""

    def __init__(self, id, message):
        self.id = id
        self.message = message

    def __str__(self):
        return f"BadIdError: id: {self.id}, message: {self.message}"
    

class BadNameError(Exception):
    """Класс для обработки ошибок неверно введённого имени для задачи."""

    def __init__(self, Name, message):
        self.Name = Name
        self.message = message

    def __str__(self):
        return f"BadNameError: Name: {self.Name}, message: {self.message}"
    

class Task:
    """Класс для задач."""
    def __init__(self, tname, tpriority):
        self.tname = tname
        self.tpriority = tpriority
    
    def __str__(self):
        return f"name: {self.tname}, priority: {self.tpriority}"
    

class TodoList:
    """Класс по всему списку с делами."""
    __auto_id = 1

    def __init__(self):
        self.__task_storage: dict[Task] = {}

    @classmethod
    def incrId(cls):
        cls.__auto_id += 1

    @classmethod
    def getId(cls):
        return cls.__auto_id
    
    def create(self, tname, tpriority):
        """Метод по созданию задачи в место их хранения."""
        if len(tname) < 7:
            raise BadNameError(tname, "Имя должно быть более 7 символов!")
        
        if tpriority < 1 or tpriority > 100:
            raise BadPriorityError(tpriority, "Приоритет должен быть в диапазоне от 1 до 100!")
        
        self.__task_storage.update({TodoList.getId(): Task(tname, tpriority)})
        TodoList.incrId()
        return True
    
    def read(self, tid):
        """Метод по чтению задачи по их id."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи НЕ содержится!")
        
        return self.__task_storage.get(tid)
    
    def readall(self):
        """Метод по чтению всех задач."""
        res_str = "Номер задачи: значение\n"
        for k,v in self.__task_storage.items():
            res_str += f"{k} | {v}\n"
        return res_str

    def update(self, tid, name, priority):
        """Метод по обновлению задачи в месте её хранения."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи НЕ содержится!")
        
        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов!")
        
        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100!")
        
        self.__task_storage.update({tid: Task(name, priority)})

        return True
    
    def delete(self, tid):
        """Метод по удалению задачи по id."""

        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи НЕ содержится!")
        
        self.__task_storage.pop(tid)

        return True
    
class App:
    def __init__(self, TodoListInst):
        self.__todolist = TodoListInst

    def Run(self):
        """Основной метод по для работы сценария."""

        condition = input(App.condition_display())
        while condition != "-1":
            try:
                # Создание задачи.
                if condition == "1":
                    name = input("Введите имя: ")
                    priority = int(input("Введите приоритет: "))
                    self.__todolist.create(name, priority)
                
                # Просмотр всех задач.
                elif condition == "2":
                    print(self.__todolist.readall())

                # Просмотр определённой задачи.
                elif condition == "3":
                    id = int(input("Введите индекс: "))
                    print(self.__todolist.read(id))

                # Обновление задачи.
                elif condition == "4":
                    id = int(input("Введите индекс: "))
                    tname = input("Введите имя: ")
                    tpriority = int(input("Введите приоритет: "))
                    self.__todolist.update(id,tname,tpriority)

                # Удаление задачи.
                elif condition == "5":
                    id = int(input("Введите индекс: "))
                    self.__todolist.delete(id)

                # Вывод на иной случай.
                else:
                    print("Неизвестная ошибка.")
                    print(App.condition_display())

            except BadIdError as e:
                print("Проблема: ", e)
            except BadPriorityError as e:
                print("Проблема: ", e)
            except BadNameError as e:
                print("Проблема: ", e)
            except Exception as e:
                print("Неизвестная проблема! ", e)
            else:
                print("Операция прошла успешно")

            condition = input("Выберете операцию: ")
        
        print("This is the end..\nBye Bye.")

    @staticmethod
    def condition_display():
        """Меню для пользователя."""
        return """
        Номер задачи(от 1)
        Имя задачи(не менее 7 символов)
        Приоритет(от 1 до 100)
        1 - create - добавление новой задачи,
        2 - readall - просмотр списка задач,
        3 - read - просмотр задачи по id,
        4 - update - обновление задачи по id,
        5 - delete - удаление задачи по id,
        -1 - exit - выход из программы.
        """