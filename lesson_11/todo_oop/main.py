from todo_module import TodoList, App


def main():
    """Главный цикл по вызову функций."""
    
    td1 = TodoList()
    app = App(td1)
    app.Run()


if __name__ == "__main__":
    main()