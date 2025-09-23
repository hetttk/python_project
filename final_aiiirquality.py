
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Open/Generate', 'Snapshot', 'Fix data', 'Numbers', 'Plot room', 'Stop']

class AirqualityTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def quickstats(self, path):
        if not os.path.exists(path):
            d=pd.date_range("2023-03-01", periods=150, freq="D")
            tmp=pd.DataFrame({
                "date":d,
                "city":np.random.choice(["Alpha","Beta","Gamma","Delta"], len(d)),
                "AQI":np.random.randint(35,320,len(d)),
                "PM25":np.random.uniform(5,180,len(d)),
                "PM10":np.random.uniform(10,230,len(d)),
                "Temp":np.random.uniform(10,40,len(d))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def wash(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def look(self):
        if self.df.empty: return
        self.df = self.df.drop_duplicates();
        self.df.fillna(method="ffill", inplace=True)

    def loadit(self):
        if self.df.empty: return
        print("AQI std:", round(float(self.df["AQI"].std()),2))

    def drawit(self):
        if self.df.empty: return
        plt.figure(); self.df.groupby("city")[["PM25","PM10"]].mean().plot(kind="bar"); plt.title("BAR view"); plt.tight_layout(); plt.savefig("airquality_04_bar.png"); plt.close()
        plt.figure(); self.df.groupby(self.df["date"].dt.to_period("W"))["AQI"].mean().plot(); plt.ylabel("AQI weekly avg"); plt.title("LINE view 2"); plt.tight_layout(); plt.savefig("airquality_04_line.png"); plt.close()

def route(app, key):
    if key=="1": 
        app.quickstats(input("csv: ") or "airquality.csv"); print("loaded")
    elif key=="2": app.wash()
    elif key=="3": app.look(); print("done")
    elif key=="4": app.loadit()
    elif key=="5": app.drawit(); print("charts ok")
    else: print("nope")
def main():
    app=AirqualityTool()
    while True:
        print("\n[Mini Studio] ->", ITEMS)
        key=input("pick #: ").strip()
        if key=="6": print("see ya"); break
        route(app, key)

if __name__ == "__main__":
    main()
