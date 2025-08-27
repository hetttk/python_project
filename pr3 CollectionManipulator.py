records = []

while True:
    print("\nMenu:\n1) Add Student\n2) Display All Students\n3) Update Student Information\n4) Delete Student\n5) Display Subjects Offered\n6) Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        sid = int(input("ID: "))
        nm = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("DOB (YYYY-MM-DD): ")
        subj_line = input("Subjects (csv): ")
        pair = (sid, dob)
        subs = [s.strip() for s in subj_line.split(",") if s.strip()]
        subs = list(set(subs))
        d = {"pair": pair, "name": nm, "age": age, "grade": grade, "subjects": subs}
        records.append(d)
        print("Student added.")
    elif ch == "2":
        if not records:
            print("Nothing to show.")
        else:
            print("\n== Students ==")
            for d in records:
                rid, rdb = d["pair"]
                # .format() style
                line = "Student ID: {0} | Name: {1} | Age: {2} | Grade: {3} | DOB: {4} | Subjects: {5}".format(
                    rid, d["name"], d["age"], d["grade"], rdb, ", ".join(d["subjects"]))
                print(line)
    elif ch == "3":
        target = int(input("Enter ID to update: "))
        ok = False
        for d in records:
            if d["pair"][0] == target:
                ok = True
                print("Change 1) Age  2) Subjects")
                what = input("Pick: ")
                if what == "1":
                    d["age"] = int(input("New Age: "))
                elif what == "2":
                    d["subjects"] = list(set([p.strip() for p in input("New subjects: ").split(",") if p.strip()]))
                print("Done.")
                break
        if not ok:
            print("ID not found.")
    elif ch == "4":
        target = int(input("Enter ID to delete: "))
        pos = -1
        for i in range(len(records)):
            if records[i]["pair"][0] == target:
                pos = i
                break
        if pos != -1:
            del records[pos]
            print("Deleted.")
        else:
            print("Could not find.")
    elif ch == "5":
        ss = set()
        for d in records:
            ss.update(d["subjects"])
        print("Unique Subjects:", ", ".join(sorted(ss)) if ss else "None")
    elif ch == "6":
        print("Thanks for using the organizer.")
        break
    else:
        print("Wrong choice.")
