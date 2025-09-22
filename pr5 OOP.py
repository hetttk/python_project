
class PersonX:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        cls = "PersonX"
        return f"{cls}(name={self.name}, age={self.age})"

class EmployeeX(PersonX):
    def __init__(self, name, age, code="", pay=0.0):
        super().__init__(name, age)
        self.__badge = str(code)
        self.__package = float(pay)

    # encapsulation
    def code(self): return self.__badge
    def code_set(self, new_code): self.__badge = str(new_code)
    def pay(self): return self.__package
    def pay_set(self, value):
        value = float(value)
        if value < 0: print("Invalid pay")
        else: self.__package = value

    # 'overloading' via alternative constructors
    @classmethod
    def from_core(cls, name, age, code):
        return cls(name, age, code, 0.0)
    @classmethod
    def hydrate(cls, d):
        return cls(d.get("name",""), d.get("age",0), d.get("employee_id",""), d.get("salary",0))

    def __str__(self):
        return f"EmployeeX(name={self.name}, age={self.age}, code={self.__badge}, pay=${self.__package})"
    # comparison operators -> pay based
    def __eq__(self, other): return isinstance(other, EmployeeX) and self.pay() == other.pay()
    def __lt__(self, other): return isinstance(other, EmployeeX) and self.pay() < other.pay()
    def __gt__(self, other): return isinstance(other, EmployeeX) and self.pay() > other.pay()

    def present(self): print(self)

class ManagerX(EmployeeX):
    def __init__(self, name, age, code, pay, dept):
        super().__init__(name, age, code, pay)
        self.dept = dept
    def present(self):
        print(super().__str__() + " | team: " + str(self.dept))

class DeveloperX(EmployeeX):
    def __init__(self, name, age, code, pay, lang):
        super().__init__(name, age, code, pay)
        self.lang = lang
    def present(self):
        print(super().__str__() + " | code lang: " + str(self.lang))

print("check:", issubclass(ManagerX, EmployeeX), issubclass(DeveloperX, EmployeeX))

crowd_box = []
book_box = {}

def banner():
    print("\n--- Workforce Panel ---")
    print("1) New PersonX")
    print("2) New EmployeeX")
    print("3) New ManagerX")
    print("4) New DeveloperX")
    print("5) Show")
    print("6) Compare Pay")
    print("7) Exit")

while True:
    banner()
    pick = input("Choose: ").strip()
    if pick == "1":
        nm = input("Name: "); ag = int(input("Age: "))
        crowd_box.append(PersonX(nm, ag))
        print("saved")
    elif pick == "2":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: "))
        e = EmployeeX(nm, ag, cd, py); book_box[e.code()] = e; print("ok")
    elif pick == "3":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: ")); dp = input("Team: ")
        m = ManagerX(nm, ag, cd, py, dp); book_box[m.code()] = m; print("ok")
    elif pick == "4":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: ")); lg = input("Code Lang: ")
        d = DeveloperX(nm, ag, cd, py, lg); book_box[d.code()] = d; print("ok")
    elif pick == "5":
        print("a) PersonXs  b) EmployeeX by id  c) all EmployeeX")
        sub = input("-> ").strip().lower()
        if sub == "a":
            if not crowd_box: print("none")
            for i, p in enumerate(crowd_box, 1): print(i, p)
        elif sub == "b":
            key = input("id: "); obj = book_box.get(key)
            if obj: obj.present()
            else: print("not found")
        else:
            if not book_box: print("empty")
            for v in book_box.values(): v.present()
    elif pick == "6":
        a = input("id1: "); b = input("id2: ")
        x = book_box.get(a); y = book_box.get(b)
        if not x or not y: print("missing")
        else:
            if x == y: print("same pay")
            elif x > y: print(a, "earns more than", b)
            else: print(a, "earns less than", b)
    elif pick == "7":
        print("bye"); break
    else:
        print("wrong")
