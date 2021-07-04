from core.pyba_logic import PybaLogic


class TaskLogic(PybaLogic):
    def __init__(self):
        super().__init__()
        self.table = "task"

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
            return []

    def insert(self, task):
        database = self.createDatabaseObj()
        sql = f"insert into {self.table} (id, description) values(0,'{task['description']}');"
        rows = database.executeNonQueryRows(sql)
        return rows

    def update(self, id, task):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE {self.table} "
            + f"SET description = '{task['description']}'  "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def delete(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from {self.table} where id={id}"
        rows = database.executeNonQueryRows(sql)
        return rows
