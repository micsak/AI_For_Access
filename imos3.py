import requests
import pandas as pd
import io
from pathlib import Path

# --- Config ---
mytoken = "af8b1dfa25bfbe6b4f88e3b8708a7558bc4445b890d2a83ce5dbed56923f3114"
url = f"https://api.veslink.com/v1/imos/reports/DailyPositionReport?apiToken={mytoken}"

# --- Fetch ---
resp = requests.get(url)
resp.raise_for_status()  # fail fast if HTTP error

# --- Parse (JSON or CSV) ---
try:
    data = resp.json()
    df = pd.json_normalize(data)
except Exception:
    df = pd.read_csv(io.StringIO(resp.text))

# --- Save to a known folder inside your workspace ---
outdir = Path.cwd() / "outputs"
outdir.mkdir(parents=True, exist_ok=True)

sample_xlsx = outdir / "daily_position_report_sample.xlsx"
full_xlsx   = outdir / "daily_position_report_full.xlsx"
sample_csv  = outdir / "daily_position_report_sample.csv"
full_csv    = outdir / "daily_position_report_full.csv"

df.head(10).to_excel(sample_xlsx, index=False)
df.to_excel(full_xlsx, index=False)
df.head(10).to_csv(sample_csv, index=False)
df.to_csv(full_csv, index=False)

print("Saved files:")
print(sample_xlsx.resolve())
print(full_xlsx.resolve())
print(sample_csv.resolve())
print(full_csv.resolve())

print("\nCurrent working directory:", Path.cwd().resolve())
