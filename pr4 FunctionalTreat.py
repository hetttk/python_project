
store = {"type":"1D","box":[]}

def take_input():
    """Collect numbers for 1D or 2D list."""
    global store
    k = input("Enter 1 for 1D, 2 for 2D: ").strip()
    if k == "2":
        rr = int(input("Rows count: "))
        m = []
        for i in range(rr):
            # avoiding outer formatting by building the prompt string
            prompt = "Row " + str(i+1) + ": "
            m.append([int(q) for q in input(prompt).split()])
        store = {"type":"2D","box":m}
    else:
        store = {"type":"1D","box":[int(a) for a in input("Give numbers: ").split()]}
    print("Stored.")

def show_basic():
    """Built-in functions over the current dataset."""
    if store["type"]=="1D":
        a = store["box"]
        if not a: print("empty"); return
        print(f"len={len(a)} min={min(a)} max={max(a)} sum={sum(a)} avg={round(sum(a)/len(a),2)}")
    else:
        g = store["box"]; flat=[n for r in g for n in r]
        if not flat: print("empty"); return
        print("rows", len(g), "items", len(flat), "min", min(flat), "max", max(flat), "sum", sum(flat), "avg", round(sum(flat)/len(flat),2))
        for r in g: print(r)

def rec_fact(n):
    """Recursively compute factorial."""
    return 1 if n<2 else n*rec_fact(n-1)

def run_rec():
    """Ask and print factorial."""
    val = int(input("number: "))
    print("factorial:", rec_fact(val))

def filt_with_lambda():
    """Filter using lambda then map to squares."""
    if store["type"]!="1D": print("Switch to 1D."); return
    arr = store["box"]
    if not arr: print("empty"); return
    t = int(input("threshold: "))
    kept = list(filter(lambda x:x>=t, arr))
    sq = list(map(lambda x:x*x, kept))
    print("kept:", kept); print("squared:", sq)

def dataset_stats():
    """Return multiple stats."""
    seq = store["box"] if store["type"]=="1D" else [n for r in store["box"] for n in r]
    if not seq: return None
    return min(seq), max(seq), sum(seq), sum(seq)/len(seq)

def sort_now():
    """Sort in place (1D) or per-row copy (2D)."""
    if store["type"]=="1D":
        a = store["box"]
        order = input("asc(1) or desc(2): ")
        a.sort(reverse=(order=="2"))
        print("sorted:", a)
    else:
        g = store["box"]
        newg = [sorted(r, reverse=False) for r in g]
        print("new sorted grid:"); [print(row) for row in newg]

def print_kwargs(**k):
    """Demo of **kwargs printing"""
    for key,val in k.items(): print(key, "=", val)

def print_args(*a):
    """Demo of *args printing"""
    print("args:", a)


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

def docs_menu():
    """Show docstrings for quick help."""
    for f in [take_input, show_basic, run_rec, filt_with_lambda, sort_now, dataset_stats, print_args, print_kwargs]:
        print("-", f.__name__, ":", (f.__doc__ or "").strip())

while True:
    show_menu()
    z = input("choose: ")
    if z=="1": take_input()
    elif z=="2": show_basic()
    elif z=="3": run_rec()
    elif z=="4": filt_with_lambda()
    elif z=="5": sort_now()
    elif z=="6":
        r = dataset_stats()
        if r:
            mn,mx,sm,av = r
            print_args(mn,mx,sm,round(av,2))
            print_kwargs(minimum=mn, maximum=mx, total=sm, average=round(av,2))
        else: print("empty")
    elif z=="7": docs_menu()
    elif z=="8": print("Thanks, bye!"); break
    else: print("again please")
