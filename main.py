

def add_task(task):
     print(f"added {task}")

# def update_task():

# def delete_task():


def main():
    while True:
        user_input = input("#")
        if "add" in str(user_input):
            add_task(user_input[4:])


if __name__ == "__main__":
     main()
