from abc import ABC, abstractmethod

class Db_connect(ABC):
    def __init__(self, user, port, database, password, attributes):
        pass
    def connect(self):
        pass
    def execute_query(self):
        pass
    def close(self):
        pass
class Mydb(Db_connect):
    @abstractmethod
    def __init__(self, user, port, database, password, attributes):
        self.user = user
        self.port = port
        self.database = database
        self.password = password
        self.attributes = attributes
    @abstractmethod
     
    def connect(self):
        print("connecting")
    @abstractmethod

    def execute_query(self):
        print("executing")
    @abstractmethod

    def close(self):
        print("clossing")
