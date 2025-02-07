import datetime
import json

class Task:
    def __init__(self,id=1,description=None,status="todo",created_at=str(datetime.date.today()),updated_at=str(datetime.date.today())):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def add_task(self):
        file = open('task_data.json')
        data = []
        data = json.load(file)
        data.append(self.__dict__)

        json_object = json.dumps(data, indent=0)
        with open('task_data.json', 'w') as outfile:
            outfile.write(json_object)
    
def update_task(id,update):
    file = open('task_data.json')
    data = []
    data = json.load(file)
    for tasks in data:
        if tasks["id"] == int(id):
            tasks.update({"description":update})
            tasks.update({"updated_at":str(datetime.date.today())})
    print(f"Task {id} updated")
    json_object = json.dumps(data, indent=0)
    with open('task_data.json', 'w') as outfile:
        outfile.write(json_object)



def list():
    file = open('task_data.json')
    data = json.load(file)
    print(data)

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




# def delete_task():


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


if __name__ == "__main__":
     main()
