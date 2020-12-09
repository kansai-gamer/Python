class TaskException(Exception):
    pass

class Task:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class Employee:
    def work(self, task):
        if task.volume <= 5:
            print("Employee work:", task.name)
        else:
            raise TaskException()

class Manager:
    def set_empoloyee(self, employee):
        self.empoloyee = employee

    def work(self, task):
        try:
            self.empoloyee.work(task)
        except TaskException as e:
            if task.volume >= 50:
                raise e
            print("Manager work: ", task.name)
class President:
    def set_manager(self, manager):
        self.manager = manager

    def work(self, task):
        try:
            self.manager.work(task)
        except:
            print("President work: ", task.name)

task1 = Task("small task", 1)
task2 = Task("Medium task", 10)
task3 = Task("Large Task", 100)

tanaka = Employee()
murayama = Manager()
sato = President()
sato.set_manager(murayama)
murayama.set_empoloyee(tanaka)

sato.work(task1)
sato.work(task2)
sato.work(task3)