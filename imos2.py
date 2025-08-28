import requests
import pandas as pd
import io

mytoken = "af8b1dfa25bfbe6b4f88e3b8708a7558bc4445b890d2a83ce5dbed56923f3114"
url = f"https://api.veslink.com/v1/imos/reports/DailyPositionReport?apiToken={mytoken}"

response = requests.get(url)

print("Status code:", response.status_code)
print("Content type:", response.headers.get("Content-Type", ""))

df = None
try:
    # Try JSON first
    data = response.json()
    df = pd.json_normalize(data)
except Exception:
    # If not JSON, try CSV
    df = pd.read_csv(io.StringIO(response.text))

# Print only first 10 rows
print(df.head(10))
