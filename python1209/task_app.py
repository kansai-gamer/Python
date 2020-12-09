import datetime

class Task:
    STATUS_CLOSED = 0
    STATUS_OPENED = 1

    def __init__(self, id, title, date, status):
        self.id = id
        self.title = title
        self.date = date
        self.status = status

    def show(self):
        print(self.id, self.title, self.date, self.status)

class TaskBoardError(Exception):
    pass

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

    def edit_task(self, id, title, status):
        for task in self.task_list:
            edit_flag = False
            if task.id == id:
                task.title = title
                task.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                task.status = status
                edit_flag = True

        if edit_flag == False:
            raise TaskBoardError()

    def delete_task(self, id):
        try:
            self.task_list.pop(id)
        except IndexError:
            raise TaskBoardError()
    
    def save_file(self, file_name):
        self.file_name = file_name
        f = open(file_name,'w')
        for task in self.task_list:
            f.write(str(task.id)+ "," + str(task.title)+ "," + str(task.date) + "," + str(task.status)+ "\n")
        f.close()

    def load_file(self, file_name):
        with open(file_name) as f:
            s = f.readlines
            
        

if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.load_file("task.csv")
    task_board.show_task_list()