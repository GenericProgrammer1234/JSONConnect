import os

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
    parts = txt.split()
    command = parts[0]

    if command == "create":
        if len(parts) > 2 and parts[2] == "if":
            condition = parts[2:]
            res = parse_condition(condition)
            if res is True:
                try:
                    with open(f"{parts[1]}.json", "x"):
                        pass
                    print(f"Database `{parts[1]}` created")
                except IndexError:
                    print("No name for the database provided")
                except FileExistsError:
                    print("Database already exists")
            elif res == "invc":
                print("Invalid condition")
        else:
            try:
                with open(f"{parts[1]}.json", "x"):
                    pass  # Create an empty file
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
            elif res == "invc":
                print("Invalid condition")
        else:
            try:
                os.remove(f"{parts[1]}.json")
                print(f"Database `{parts[1]}` deleted")
            except IndexError:
                print("Database doesn't exist")
    elif command == "if":
        print("true" if parse_condition(parts) else "false")
    else:
        print(f"Command doesn't exist: {command}")

while True:
    txt = input("> ")
    parse(txt)
