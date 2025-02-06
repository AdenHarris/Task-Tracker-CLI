import json

def add_task(task):
    print(f"added {task}")
    x = {
        "id": 1,
        "description":"description of task",
        "status":"todo",
        "createdAt":"date",
        "updatedAt":"date"
         }
    
    json_object = json.dumps(x)

    with open('task_data.json', 'w') as outfile:
        outfile.write(json_object)
    
def list():
    file = open('task_data.json')
    data = json.load(file)
    print(data)

# def update_task():

# def delete_task():


def main():
    while True:
        user_input = input("#")
        if "add" in str(user_input):
            add_task(user_input[4:])
        if user_input == "list":
            list()


if __name__ == "__main__":
     main()
