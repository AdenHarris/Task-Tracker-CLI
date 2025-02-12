import datetime
import json

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
    
def update_task(id,update):
    data = read_json_to_dict()
    for tasks in data:
        if tasks["id"] == int(id):
            tasks.update({"description":update})
            tasks.update({"updated_at":str(datetime.date.today())})
    print(f"Task {id} updated")
    write_to_json(data)

def mark_in_progress(id):
    data = read_json_to_dict()
    for tasks in data:
        if tasks["id"] == int(id):
            tasks.update({"status":"in progress"})
            tasks.update({"updated_at":str(datetime.date.today())})
    print(f"Task {id} updated")
    write_to_json(data)

def mark_done(id):
    data = read_json_to_dict()
    for tasks in data:
        if tasks["id"] == int(id):
            tasks.update({"status":"done"})
            tasks.update({"updated_at":str(datetime.date.today())})
    print(f"Task {id} updated")
    write_to_json(data)

def delete_task(id):
    data = read_json_to_dict()
    for tasks in data:
        if tasks["id"] == int(id):
            data.remove(tasks)
    print(f"Task {id} Removed")
    write_to_json(data)


def list():
    data = []
    data = read_json_to_dict()
    sorted_tasks = sorted(data, key=lambda x: (x['id']))
    for tasks in sorted_tasks:
        print(f"Task {tasks["id"]} '{tasks["description"]}' {tasks["status"]}")


#reads json file to determine amount of existing tasks
def load_json_file():
    file = open('task_data.json')
    data = []
    data.append(json.load(file))
    print(len(data[0]))

    if len(data[0]) == 0:
        return 1
    else:
        return len(data[0]) + 1


def main():
    id_counter = load_json_file()
    while True:
        user_input = input("#")
        if "add" in str(user_input):
            task = Task(id=id_counter, description=user_input[4:])
            #test_task = Task(1,"test","todo","today","today")
            task.add_task()
            print(f"Task added successfully (ID:{task.id})")
            id_counter += 1
        if user_input == "list":
            list()
        
        if "update" in str(user_input):
            update_task(user_input[7],user_input[9:])

        if "mark-in-progress" in str(user_input):
            mark_in_progress(user_input[17])
        
        if "mark-done" in str(user_input):
            mark_done(user_input[10])        
        
        if "delete" in str(user_input):
            delete_task(user_input[7])
            id_counter = load_json_file()


if __name__ == "__main__":
     main()
