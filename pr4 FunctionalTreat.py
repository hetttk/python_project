
DATAHUB = {"style":"1D","nums":[]}

def load_data():
    """Enter numbers for 1D or 2D list."""
    global DATAHUB
    kind = input("1 for 1D, 2 for 2D: ")
    if kind=="2":
        m=int(input("rows: ")); table=[]
        for r in range(m):
            table.append([int(s) for s in input("row-"+str(r+1)+": ").split()])
        DATAHUB={"style":"2D","nums":table}
    else:
        DATAHUB={"style":"1D","nums":[int(s) for s in input("values: ").split()]}
    print("data loaded")

def builtins():
    """Use built-in functions to summarize the data."""
    if DATAHUB["style"]=="1D":
        arr=DATAHUB["nums"]; 
        if not arr: print("empty"); return
        print(f"len={len(arr)} min={min(arr)} max={max(arr)} sum={sum(arr)} avg={round(sum(arr)/len(arr),2)}")
    else:
        g=DATAHUB["nums"]; flat=[n for r in g for n in r]
        if not flat: print("empty"); return
        print("total",len(flat),"min",min(flat),"max",max(flat),"sum",sum(flat))
        for r in g: print(r)

def recu(n): 
    """factorial recursion simple"""
    return 1 if n<=1 else n*recu(n-1)

def factorial_menu():
    """Ask for n and print n!"""
    n=int(input("number: ")); print("n!=",recu(n))

def lam():
    """lambda + filter/map to keep <= threshold then cube"""
    if DATAHUB["style"]!="1D": print("need 1D"); return
    a=DATAHUB["nums"]; 
    if not a: print("empty"); return
    t=int(input("keep values <= : "))
    kept=list(filter(lambda x:x<=t,a))
    print("kept:",kept); print("cubed:",list(map(lambda x:x**3,kept)))

def bundle():
    """return multiple stats"""
    seq=DATAHUB["nums"] if DATAHUB["style"]=="1D" else [n for r in DATAHUB["nums"] for n in r]
    if not seq: return None
    return min(seq),max(seq),sum(seq),sum(seq)/len(seq)

def organize():
    """sort 1D with .sort(); 2D make new sorted rows"""
    if DATAHUB["style"]=="1D":
        a=DATAHUB["nums"]
        if not a: print("empty"); return
        way=input("1 asc / 2 desc: ")
        a.sort(reverse=(way=="2")); print("sorted:",a)
    else:
        print("sorted copy of rows:")
        for r in [sorted(r) for r in DATAHUB["nums"]]: print(r)

def A(*a): print("args:",a)
def K(**k): print("info:",k)


def show_menu():
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Help: Function Docs")
    print("8. Exit Program")

def docsx():
    for f in [load_data,builtins,factorial_menu,lam,organize,bundle,A,K]:
        print("-", f.__name__, ":", (f.__doc__ or "").strip())

while True:
    show_menu()
    cc=input(">> ")
    if cc=="1": load_data()
    elif cc=="2": builtins()
    elif cc=="3": factorial_menu()
    elif cc=="4": lam()
    elif cc=="5": organize()
    elif cc=="6":
        r=bundle()
        if r: mn,mx,sm,av=r; A(mn,mx,sm,round(av,2)); K(minimum=mn,maximum=mx,total=sm,average=round(av,2))
        else: print("no data")
    elif cc=="7": docsx()
    elif cc=="8": print("closing..."); break
    else: print("invalid")
