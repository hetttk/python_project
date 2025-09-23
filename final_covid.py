
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Fetch data', 'Show head/tail', 'Wash data', 'Lite metrics', 'Paint graphs', 'Bye']

class CovidTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def wash(self, path):
        if not os.path.exists(path):
            days=pd.date_range("2020-04-01", periods=120, freq="D")
            tmp=pd.DataFrame({
                "date":days,
                "country":np.random.choice(list("ABCD"), len(days)),
                "cases":np.random.randint(30,3000,len(days)),
                "deaths":np.random.randint(0,120,len(days)),
                "recovered":np.random.randint(10,2500,len(days))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def drawit(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def quickstats(self):
        if self.df.empty: return
        for c in self.df.columns:
            if self.df[c].dtype.kind in "biufc": self.df[c].fillna(self.df[c].median(), inplace=True)
            else: self.df[c].fillna("Unknown", inplace=True)

    def look(self):
        if self.df.empty: return
        print("peak cases:", int(self.df["cases"].max())); print("mean deaths:", round(float(self.df["deaths"].mean()),2))

    def loadit(self):
        if self.df.empty: return
        plt.figure(); self.df.set_index("date")[["cases","recovered"]].plot(kind="area", alpha=0.5); plt.title("AREA view"); plt.tight_layout(); plt.savefig("covid_04_area.png"); plt.close()
        plt.figure(); self.df.plot(kind="scatter", x="cases", y="deaths"); plt.title("SCATTER view 2"); plt.tight_layout(); plt.savefig("covid_04_scatter.png"); plt.close()

def route(app, key):
    if key=="1": 
        app.wash(input("csv: ") or "covid.csv"); print("loaded")
    elif key=="2": app.drawit()
    elif key=="3": app.quickstats(); print("done")
    elif key=="4": app.look()
    elif key=="5": app.loadit(); print("charts ok")
    else: print("nope")
def main():
    app=CovidTool()
    while True:
        print("\n[Pocket Suite] ->", ITEMS)
        key=input("pick #: ").strip()
        if key=="6": print("see ya"); break
        route(app, key)

if __name__ == "__main__":
    main()
