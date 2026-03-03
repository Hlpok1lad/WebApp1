import json
import os
FILE_NAME = 'ToDoList.json'

def load_data():
    global toDoList  # Tell the function to use the list outside
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            toDoList = json.load(f)
            return toDoList
    else:
        return []


def save_data():

    with open(FILE_NAME, 'w') as f:
        json.dump(toDoList, f)
toDoList = []
doneList = []