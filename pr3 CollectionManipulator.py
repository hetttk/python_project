kids = []

while True:
    print("\n1-Add 2-Show 3-Update 4-Delete 5-Subjects 6-Exit")
    c = input("Enter: ")

    if c == "1":
        no = int(input("ID: "))
        nm = input("Name: ")
        ag = int(input("Age: "))
        gd = input("Grade: ")
        born = input("DOB (YYYY-MM-DD): ")
        sj = input("Subjects (csv): ")
        lock = (no, born)
        subjects = list(set([w.strip() for w in sj.split(",") if w.strip()]))
        kids.append({"key": lock, "name": nm, "age": ag, "grade": gd, "subjects": subjects})
        print("Added.")
    elif c == "2":
        if not kids:
            print("No data.")
        else:
            for k in kids:
                rid, db = k["key"]
                print("Student ID: {0} | Name: {1} | Age: {2} | Grade: {3} | DOB: {4} | Subjects: {5}".format(
                    rid, k["name"], k["age"], k["grade"], db, ", ".join(k["subjects"])))
    elif c == "3":
        keyid = int(input("ID to edit: "))
        hit = False
        for k in kids:
            if k["key"][0] == keyid:
                hit = True
                print("Change 1-Age 2-Subjects")
                w = input("Pick: ")
                if w == "1":
                    k["age"] = int(input("New age: "))
                elif w == "2":
                    k["subjects"] = list(set([p.strip() for p in input("Subjects: ").split(",") if p.strip()]))
                print("Updated.")
                break
        if not hit:
            print("ID not found.")
    elif c == "4":
        keyid = int(input("ID to remove: "))
        rm = -1
        for i in range(len(kids)):
            if kids[i]["key"][0] == keyid:
                rm = i
                break
        if rm != -1:
            del kids[rm]
            print("Deleted.")
        else:
            print("Not found.")
    elif c == "5":
        sset = set()
        for k in kids:
            sset.update(k["subjects"])
        print("Subjects offered:", ", ".join(sorted(sset)) if sset else "None")
    elif c == "6":
        print("Thanks and goodbye.")
        break
    else:
        print("Wrong choice.")
