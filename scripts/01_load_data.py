import glob, zipfile
import pandas as pd

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
frames = []
for z in sorted(glob.glob("../data/f923_*.zip")):
    year = int(z[-8:-4])
    with zipfile.ZipFile(z) as zf:
        name = [n for n in zf.namelist() if "Schedules_2_3_4_5" in n and n.endswith(".xlsx")][0]
        df = pd.read_excel(zf.open(name), sheet_name=0, header=5)
    df.columns = [" ".join(str(c).split()) for c in df.columns]  # 去掉列名里的换行
    wind = df[(df["Reported Fuel Type Code"] == "WND") & (df["Reported Prime Mover"] == "WT")]
    cols = ["Plant Id", "Plant State"] + [f"Netgen {m}" for m in months]
    wind = wind[cols].rename(columns={f"Netgen {m}": i + 1 for i, m in enumerate(months)})
    wind[list(range(1, 13))] = wind[list(range(1, 13))].apply(pd.to_numeric, errors="coerce")
    wind = wind.groupby(["Plant Id", "Plant State"], as_index=False).sum()  # 同一电厂合并成一行
    wind.insert(0, "Year", year)
    frames.append(wind)
    print(year, len(wind), "wind plants")
pd.concat(frames).to_csv("../data/wind_netgen_monthly.csv", index=False)
