import datetime
import json
import os
import traceback

def read_json_to_dict():
    file = open('task_data.json')
    data = []
    data = json.load(file)
    return data

def write_to_json(data):
    json_object = json.dumps(data, indent=0)
    with open('task_data.json', 'w') as outfile:
        outfile.write(json_object)

class Task:
    def __init__(self,id=1,description=None,status="todo",created_at=str(datetime.date.today()),updated_at=str(datetime.date.today())):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def add_task(self):
        data = read_json_to_dict()
        self.id = 1
        for tasks in data:
            if tasks.get("id") == self.id:
                self.id += 1
        data.append(self.__dict__)
        write_to_json(data)
        print(f"Task added successfully (ID:{self.id})")
    
def update_task(id,update,status):
    data = read_json_to_dict()
    for tasks in data:
        if tasks["id"] == int(id):
            tasks.update({"updated_at":str(datetime.date.today())})

            if status == "in progress":
                tasks.update({"status":"in progress"})

            elif status == "done":
                tasks.update({"status":"done"})

            else:
                tasks.update({"description":update})
            print(f"Task {id} updated")

    write_to_json(data)

def delete_task(id):
    data = read_json_to_dict()
    for tasks in data:
        if tasks["id"] == int(id):
            data.remove(tasks)
            print(f"Task {id} Removed")
    write_to_json(data)

def list(status=None):
    data = []
    data = read_json_to_dict()
    sorted_tasks = sorted(data, key=lambda x: (x['id']))
    for tasks in sorted_tasks:
        if status == None:
            print(f"Task {tasks["id"]} '{tasks["description"]}' {tasks["status"]}")
        elif tasks["status"] == status:
            print(f"Task {tasks["id"]} '{tasks["description"]}' {tasks["status"]}")


#reads json file to determine amount of existing tasks
def load_json_file():
    if not os.path.exists('task_data.json'):
        new_file = open('task_data.json', "x")
        write_to_json([])
        return 1
    else:
        file = open('task_data.json')
        data = []
        data.append(json.load(file))

    if len(data[0]) == 0:
        return 1
    else:
        return len(data[0]) + 1

def list_commands():
    print("list 'status': shows all tasks. optional filter on task status")
    print("add 'task description' : adds a new task")
    print("update 'ID' 'new task' : updates existing task")
    print("delete 'ID' : removes task")
    print("mark in progress 'ID' : sets task status to in progress")
    print("mark done 'ID' : sets task status to done")

def user_input_loop():
    id_counter = load_json_file()
    while True:
            user_input = input("#")
            try:

                if user_input[:3] == "add":
                    task = Task(id=id_counter, description=user_input[4:])
                    task.add_task()
                    id_counter += 1

                if user_input[:4] == "list":
                    if user_input[4:9] == " done":
                        list("done")
                    elif user_input[4:9] == " todo":
                        list("todo")
                    elif user_input[4:16] == " in progress":
                        list("in progress")
                    else:
                        list()
                
                if user_input[:6] == "update":
                        update_task(user_input[7],user_input[9:])

                if user_input[:16] == "mark in progress":
                        update_task(user_input[17],None, "in progress")
                        
                if user_input[:9] == "mark done":
                        update_task(user_input[10],None,"done")   

                if user_input[:6] == "delete":
                        delete_task(user_input[7])
                        id_counter = load_json_file()

                if user_input[:4] == "help":
                    list_commands()
            except:
                traceback.print_exc()
                print("Input Error: Please check you are using correct syntax.")
            
def main():
    print("######Task-Tracker-CLI######")
    print("# Welcome!")
    print("#(type 'help' for commands)")
    user_input_loop()

if __name__ == "__main__":
     main()
