import os
import platform
import json
selected = ""

def format_json(data, prefix='', nest=1):
    for key, value in data.items():
        if isinstance(value, dict):
            if prefix != "":
                print(f"{prefix} {key}")
            else:
                print(f"{prefix}{key}")
            format_json(value, prefix='---' * nest, nest=nest+1)
        else:
            if prefix != "":
                print(f"{prefix} {key} | {value}")
            else:
                print(f"{prefix}{key} | {value}")

def parse_condition(txt):
    if txt[0] == "if":
        try:
            obj = txt[1]
        except IndexError:
            print("Object does not exist")
            return
        if len(txt) > 2 and txt[2] == "exists":
            return os.path.isfile(f"{obj}.json")
        return "invc"
    return None

def parse(txt):
    global selected
    parts = txt.split()
    command = parts[0]

    if command == "create":
        if len(parts) > 2 and parts[2] == "if":
            condition = parts[2:]
            res = parse_condition(condition)
            if res is True:
                try:
                    with open(f"{parts[1]}.json", "x") as file:
                        file.write("{}")
                    print(f"Database `{parts[1]}` created")
                except IndexError:
                    print("No name for the database provided")
                except FileExistsError:
                    print("Database already exists")
            elif res == "invc":
                print("Invalid condition")
        else:
            try:
                with open(f"{parts[1]}.json", "x") as file:
                    file.write("{}")
                print(f"Database `{parts[1]}` created")
            except IndexError:
                print("No name for the database provided")
            except FileExistsError:
                print("Database already exists")
    elif command == "delete":
        if len(parts) > 2 and parts[2] == "if":
            condition = parts[2:]
            res = parse_condition(condition)
            if res is True:
                try:
                    os.remove(f"{parts[1]}.json")
                    print(f"Database `{parts[1]}` deleted")
                except IndexError:
                    print("Database doesn't exist")
                except FileNotFoundError:
                    print("Database doesn't exist")
            elif res == "invc":
                print("Invalid condition")
        else:
            try:
                os.remove(f"{parts[1]}.json")
                print(f"Database `{parts[1]}` deleted")
            except IndexError:
                print("Database doesn't exist")
            except FileNotFoundError:
                print("Database doesn't exist")
    elif command == "select":
        if len(parts) > 2 and parts[2] == "if":
            condition = parts[2:]
            res = parse_condition(condition)
            if res is True:
                try:
                    selected = parts[1]
                    print(f"Database `{parts[1]}` selected")
                except IndexError:
                    print("Database doesn't exist")
            elif res == "invc":
                print("Invalid condition")
        else:
            try:
                selected = parts[1]
                print(f"Database `{parts[1]}` selected")
            except IndexError:
                print("Database doesn't exist")
    elif command == "insert":
        if len(parts) > 2 and parts[2] == "if":
            condition = parts[2:]
            res = parse_condition(condition)
            if res is True:
                try:
                    with open(f"{selected}.json", "r") as file:
                        data = json.load(file)
                    data[parts[1]] = parts[2]
                    with open(f"{selected}.json", "w") as file:
                        json.dump(data, file)
                    print(f"Key `{parts[1]}` with the value `{parts[2]}` inserted")
                except IndexError:
                    print("Key or value not provided")
            elif res == "invc":
                print("Invalid condition")
        else:
            try:
                with open(f"{selected}.json", "r") as file:
                    data = json.load(file)
                data[parts[1]] = parts[2]
                with open(f"{selected}.json", "w") as file:
                    json.dump(data, file)
                print(f"Key `{parts[1]}` with the value `{parts[2]}` inserted")
            except IndexError:
                print("Key or value not provided")
    elif command == "show":
        if len(parts) > 2 and parts[2] == "if":
            condition = parts[2:]
            res = parse_condition(condition)
            if res is True:
                    with open(f"{selected}.json", "r") as file:
                        data = json.load(file)
                        format_json(data)
            elif res == "invc":
                print("Invalid condition")
        else:
            with open(f"{selected}.json", "r") as file:
                data = json.load(file)
                format_json(data)      
    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    elif command == "quit":
        exit()
    elif command == "if":
        print("true" if parse_condition(parts) else "false")
    else:
        print(f"Command doesn't exist: {command}")

while True:
    txt = input("> ")
    if txt:
        parse(txt)
