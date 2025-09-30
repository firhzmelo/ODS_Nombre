class User:
    def __init__(self, usr_name, name, password):
        self.usr_name = usr_name
        self.name = name
        self.password = password
        self.tasks_done = []
        self.tasks = []

class Task:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.day_done = None
        self.done = False