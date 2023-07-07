import os

def parse_txt(txt):
    parts = txt.split()
    return parts

def parse_condition(txt):
    if txt[0] == "if":
        try:
            obj = txt[1]
        except IndexError:
            print("Object does not exist")
            return
        cond = txt[2:]
        try:
            if cond[0] == "exists":
                return os.path.isfile(f"{obj}.json")
        except IndexError:
            return "invc"
    return None

def parse(txt):
    txt = parse_txt(txt)
    if txt[0] == "create":
        try:
            if txt[2] == "if":
                condition = txt[2:]
                res = parse_condition(condition)
                if res is True:
                    try:
                        database = open(f"{txt[1]}.json", "x")
                    except IndexError:
                        print("No name for database provided")
                        return
                    except FileExistsError:
                        print("Database already exists")
                        return
                    print(f"Database `{txt[1]}` created")
                    return
                elif res == "invc":
                    print("Invalid condition")
                return
        except IndexError:
            try:
                database = open(f"{txt[1]}.json", "x")
            except IndexError:
                print("No name for database provided")
                return
            except FileExistsError:
                print("Database already exists")
                return
            print(f"Database `{txt[1]}` created")
            return
    elif txt[0] == "delete":
        try:
            if txt[2] == "if":
                condition = txt[2:]
                res = parse_condition(condition)
                if res is True:
                    try:
                        os.remove(f"{txt[1]}.json")
                    except IndexError:
                        print("Database doesn't exist")
                        return
                    print(f"Database `{txt[1]}` deleted")
                    return
                elif res == "invc":
                    print("Invalid condition")
                return
        except IndexError:
            try:
                os.remove(f"{txt[1]}.json")
            except IndexError:
                print("Database doesn't exist")
                return
            print(f"Database `{txt[1]}` deleted")
            return
    elif txt[0] == "if":
        print("true" if parse_condition(txt) else "false")
        return
    print(f"Command doesn't exist: {txt[0]}")

while True:
    txt = input("> ")
    parse(txt)
