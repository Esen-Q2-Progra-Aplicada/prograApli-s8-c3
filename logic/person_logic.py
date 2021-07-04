from core.pyba_logic import PybaLogic
from logic.task_logic import TaskLogic


class PersonLogic(PybaLogic):
    def __init__(self):
        super().__init__()
        self.table = "person"

    def getAll(self):
        database = self.createDatabaseObj()
        sql = f"select * from {self.table};"
        rowList = database.executeQuery(sql)
        return rowList

    def getRegisterById(self, id):
        database = self.createDatabaseObj()
        sql = f"select * from {self.table} where id={id};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    def insert(self, person):
        database = self.createDatabaseObj()
        sql = f"insert into {self.table} (id,name,age) values(0,'{person['name']}',{person['age']});"
        rows = database.executeNonQueryRows(sql)
        return rows

    def update(self, id, person):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE {self.table} "
            + f"SET name = '{person['name']}', age = {person['age']}  "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def delete(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from {self.table} where id={id}"
        rows = database.executeNonQueryRows(sql)
        return rows

    def insertAndCreateTask(self, person):
        rows = self.insert(person)
        logic = TaskLogic()
        task = {"description": f"process new person {person['name']} {person['age']}"}
        logic.insert(task)
        return rows
