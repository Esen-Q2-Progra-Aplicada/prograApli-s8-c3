from core.pyba_database import PybaDatabase
from logic.person_logic import PersonLogic
from logic.task_logic import TaskLogic
import pytest


def test_create_person_logic():
    logic = PersonLogic()
    assert logic is not None


@pytest.fixture()
def setup_trunctate():
    database = PybaDatabase()
    sql = "truncate table person;"
    rows = database.executeNonQueryRows(sql)
    sql = "truncate table task;"
    rows = database.executeNonQueryRows(sql)


@pytest.fixture()
def setup_trunctate_insert():
    database = PybaDatabase()
    sql = "truncate table person;"
    rows = database.executeNonQueryRows(sql)
    sql = "truncate table task;"
    rows = database.executeNonQueryRows(sql)
    sql = "insert into person (id, name, age) values(0, 'bal', 23);"
    rows = database.executeNonQueryRows(sql)


def test_getall_no_data_method(setup_trunctate):
    logic = PersonLogic()
    result = logic.getAll()
    assert result == []


def test_getall_with_data_method(setup_trunctate_insert):
    logic = PersonLogic()
    result = logic.getAll()
    assert len(result) > 0
    assert result[0]["name"] == "bal"


def test_registerById_method():
    logic = PersonLogic()
    result = logic.getRegisterById(1)
    assert result["name"] == "bal"


def test_registerById_invalidId_method():
    logic = PersonLogic()
    result = logic.getRegisterById(11)
    assert result == {}


@pytest.fixture()
def create_person():
    person = {"name": "ted", "age": 28}
    return person


def test_insert_method(create_person):
    logic = PersonLogic()
    rows = logic.insert(create_person)
    assert rows == 1
    result = logic.getRegisterById(2)
    assert result["name"] == "ted"


def test_update_method():
    logic = PersonLogic()
    person = {"name": "tedx", "age": 30}
    rows = logic.update(2, person)
    assert rows == 1
    result = logic.getRegisterById(2)
    assert result["name"] == "tedx"


def test_delete_method():
    logic = PersonLogic()
    person = {"name": "test", "age": 32}
    rows = logic.insert(person)
    assert rows == 1
    rows = logic.delete(3)
    assert rows == 1
    result = logic.getRegisterById(3)
    assert result == {}


def test_insert_createTask_method():
    logic = PersonLogic()
    person = {"name": "rob", "age": 35}
    rows = logic.insertAndCreateTask(person)
    assert rows == 1
    logic = TaskLogic()
    result = logic.getRegisterById(1)
    assert "person rob 35" in result["description"]
