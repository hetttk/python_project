
def make_file(name):
    with open(name, "x", encoding="utf-8") as f:
        f.write("")
    return True

def push_file(name, data):
    with open(name, "w", encoding="utf-8") as f:
        f.write(data)
    return True

def pull_file(name):
    with open(name, "r", encoding="utf-8") as f:
        return f.read()

def add_more(name, data):
    with open(name, "a", encoding="utf-8") as f:
        f.write(data)
    return True
