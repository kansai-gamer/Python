import datetime

class Task:
    STATUS_CLOSED = 0
    STATUS_OPENED = 1

    def __init__(self, id, title, data, status):
        self.id = id
        self.title = title
        self.data = data
        self.status = status

    def show(self):
        print(self.id, self.title, self.data, self.status)

class TaskBoard:
    def __init__(self):
        self.task_list = []

    def add_task(self, title):
        id = len(self.task_list) + 1
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = Task.STATUS_OPENED
        task = Task(id, title, date, status)
        self.task_list.append(task)

    def show_task_list(self):
        for task in self.task_list:
            task.show()

if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_task("Study Python")
    task_board.add_task("Study PHP")
    task_board.add_task("Clean the room")
    task_board.show_task_list()