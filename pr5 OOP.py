class Individual:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        cls = "Individual"
        return "{}(name={}, age={})".format(cls, self.name, self.age)

class Staffer(Individual):
    def __init__(self, name, age, code="", pay=0.0):
        super().__init__(name, age)
        self.__code = str(code)
        self.__pay = float(pay)

    # encapsulation
    def fetch_code(self): return self.__code
    def assign_code(self, new_code): self.__code = str(new_code)
    def read_salary(self): return self.__pay
    def update_salary(self, value):
        value = float(value)
        if value < 0: print("Invalid pay")
        else: self.__pay = value

    # 'overloading' via alternative constructors
    @classmethod
    def basic(cls, name, age, code):
        return cls(name, age, code, 0.0)
    @classmethod
    def from_map(cls, d):
        return cls(d.get("name",""), d.get("age",0), d.get("employee_id",""), d.get("salary",0))

    def __str__(self):
        return "Staffer(name={}, age={}, code={}, pay=${})".format(self.name, self.age, self.__code, self.__pay)
    # comparison operators -> pay based
    def __eq__(self, other): return isinstance(other, Staffer) and self.read_salary() == other.read_salary()
    def __lt__(self, other): return isinstance(other, Staffer) and self.read_salary() < other.read_salary()
    def __gt__(self, other): return isinstance(other, Staffer) and self.read_salary() > other.read_salary()

    def showup(self): print(self)

class Supervisor(Staffer):
    def __init__(self, name, age, code, pay, dept):
        super().__init__(name, age, code, pay)
        self.dept = dept
    def showup(self):
        print(super().__str__() + " | dept: " + str(self.dept))

class Programmer(Staffer):
    def __init__(self, name, age, code, pay, lang):
        super().__init__(name, age, code, pay)
        self.lang = lang
    def showup(self):
        print(super().__str__() + " | language: " + str(self.lang))

print("check:", issubclass(Supervisor, Staffer), issubclass(Programmer, Staffer))

roster = []
registry = {}

def banner():
    print("\n--- People Registry ---")
    print("1) New Individual")
    print("2) New Staffer")
    print("3) New Supervisor")
    print("4) New Programmer")
    print("5) Show")
    print("6) Compare Pay")
    print("7) Exit")

while True:
    banner()
    pick = input("Choose: ").strip()
    if pick == "1":
        nm = input("Name: "); ag = int(input("Age: "))
        roster.append(Individual(nm, ag))
        print("saved")
    elif pick == "2":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("EmpCode: "); py = float(input("Pay: "))
        e = Staffer(nm, ag, cd, py); registry[e.fetch_code()] = e; print("ok")
    elif pick == "3":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("EmpCode: "); py = float(input("Pay: ")); dp = input("Dept: ")
        m = Supervisor(nm, ag, cd, py, dp); registry[m.fetch_code()] = m; print("ok")
    elif pick == "4":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("EmpCode: "); py = float(input("Pay: ")); lg = input("Language: ")
        d = Programmer(nm, ag, cd, py, lg); registry[d.fetch_code()] = d; print("ok")
    elif pick == "5":
        print("a) Individuals  b) Staffer by id  c) all Staffer")
        sub = input("-> ").strip().lower()
        if sub == "a":
            if not roster: print("none")
            for i, p in enumerate(roster, 1): print(i, p)
        elif sub == "b":
            key = input("id: "); obj = registry.get(key)
            if obj: obj.showup()
            else: print("not found")
        else:
            if not registry: print("empty")
            for v in registry.values(): v.showup()
    elif pick == "6":
        a = input("id1: "); b = input("id2: ")
        x = registry.get(a); y = registry.get(b)
        if not x or not y: print("missing")
        else:
            if x == y: print("same pay")
            elif x > y: print(a, "earns more than", b)
            else: print(a, "earns less than", b)
    elif pick == "7":
        print("bye"); break
    else:
        print("wrong")
