from abc import ABC, abstractmethod

class Editor(ABC):
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):
    def edit(self):
        print("editing")
    def debug(self):
        print("debugging")
    def execute(self):
        print("executing")
obj = Vscode()

obj.edit()
obj.debug()
obj.execute()