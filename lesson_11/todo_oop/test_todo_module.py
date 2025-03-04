from todo_module import TodoList, BadNameError, BadPriorityError, BadIdError, App
import pytest

td = TodoList()
td.create("Go to school", 50)
td.create("Go home", 5)
td.create("play smthg", 78)


@pytest.fixture
def example_filled_todo_list():
    return td


@pytest.fixture
def example_empty_todo_list():
    return TodoList()


# Create testing.
def test_create_bad_name(example_empty_todo_list: TodoList):
    with pytest.raises(BadNameError) as e:
        example_empty_todo_list.create("ff",1)

    assert e.type is BadNameError
    assert e.value.args == ("ff", "Имя должно быть более 7 символов!")


def test_create_bad_name_str(example_empty_todo_list: TodoList):
    try:
        example_empty_todo_list.create("ff",1)
    except BadNameError as e:
        assert (
            str(e) == "BadNameError: Name: ff, message: Имя должно быть более 7 символов!"
        )


def test_create_bad_priority(example_empty_todo_list: TodoList):
    with pytest.raises(BadPriorityError) as e:
        example_empty_todo_list.create("ffffffffff",-1)

    assert e.type is BadPriorityError
    assert e.value.args == (-1, "Приоритет должен быть в диапазоне от 1 до 100!")


def test_create_bad_priority_str(example_empty_todo_list: TodoList):
    try:
        example_empty_todo_list.create("ffffffffff",-1)
    except BadPriorityError as e:
        assert (
            str(e) == "BadPriorityError: priority: -1, message: Приоритет должен быть в диапазоне от 1 до 100!"
        )


def test_create_task_ok(example_empty_todo_list: TodoList):
    assert example_empty_todo_list.create("Go to school", 50)


# Read testing.
def test_read_all(example_filled_todo_list):
    assert (example_filled_todo_list.readall() == """Номер задачи: значение
1 | name: Go to school, priority: 50
2 | name: Go home, priority: 5
3 | name: play smthg, priority: 78
""")


def test_read_bad_Id_neg(example_empty_todo_list: TodoList):
    with pytest.raises(BadIdError) as e:
        example_empty_todo_list.read(-1)

    assert e.type is BadIdError
    assert e.value.args == (-1, "Номер задачи от 1!")


def test_read_bad_Id_neg_str(example_empty_todo_list: TodoList):
    try:
        example_empty_todo_list.read(-1)
    except BadIdError as e:
        assert (
            str(e) == "BadIdError: id: -1, message: Номер задачи от 1!"
        )


def test_read_bad_id_not_contained(example_empty_todo_list: TodoList):
    with pytest.raises(BadIdError) as e:
        example_empty_todo_list.read(100)

    assert e.type is BadIdError
    assert e.value.args == (100, "Номер задачи НЕ содержится!")


def test_read_bad_Id_not_contained_str(example_empty_todo_list: TodoList):
    try:
        example_empty_todo_list.read(100)
    except BadIdError as e:
        assert (
            str(e) == "BadIdError: id: 100, message: Номер задачи НЕ содержится!"
        )


def test_read_bad_id_ok_contained(example_filled_todo_list):
    assert example_filled_todo_list.read(1).tname == "Go to school"
    assert example_filled_todo_list.read(1).tpriority == 50


def test_read_task_str(example_filled_todo_list):
    assert str(example_filled_todo_list.read(1)) == "name: Go to school, priority: 50"


# Update testing.
def test_update_task_ok(example_filled_todo_list):
    assert example_filled_todo_list.update(1, "Go to bed", 100)


def test_update_task_id_neg(example_filled_todo_list):
    with pytest.raises(BadIdError) as e:
        example_filled_todo_list.update(-1, "Go to bed", 100)

    assert e.type is BadIdError
    assert e.value.args == (-1, "Номер задачи от 1!")


def test_update_task_id_not_contained(example_filled_todo_list):
    with pytest.raises(BadIdError) as e:
        example_filled_todo_list.update(100, "Go to bed", 100)

    assert e.type is BadIdError
    assert e.value.args == (100, "Номер задачи НЕ содержится!")


def test_update_bad_priority(example_filled_todo_list):
    with pytest.raises(BadPriorityError) as e:
        example_filled_todo_list.update(1, "Go to sleep", -1)

    assert e.type is BadPriorityError
    assert e.value.args == (-1, "Приоритет должен быть в диапазоне от 1 до 100!")


def test_update_bad_name(example_filled_todo_list):
    with pytest.raises(BadNameError) as e:
        example_filled_todo_list.update(1, "ff", 2)

    assert e.type is BadNameError
    assert e.value.args == ("ff", "Имя должно быть более 7 символов!")


def test_delete_task_ok(example_filled_todo_list):
    assert example_filled_todo_list.delete(1)


def test_delete_task_id_neg(example_filled_todo_list):
    with pytest.raises(BadIdError) as e:
        example_filled_todo_list.delete(-1)

    assert e.type is BadIdError
    assert e.value.args == (-1, "Номер задачи от 1!")


def test_delete_task_id_not_contained(example_filled_todo_list):
    with pytest.raises(BadIdError) as e:
        example_filled_todo_list.delete(100)

    assert e.type is BadIdError
    assert e.value.args == (100, "Номер задачи НЕ содержится!")

