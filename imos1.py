import csv
import requests
import re

mytoken = "af8b1dfa25bfbe6b4f88e3b8708a7558bc4445b890d2a83ce5dbed56923f3114"
url = f"https://api.veslink.com/v1/imos/reports/DailyPositionReport?apiToken={mytoken}"

response = requests.get(url)


print("Status code:", response.status_code)
print("Content type:", response.headers.get("Content-Type", ""))
print("First 500 chars of response:")

print(response.text[:500])


df = None


try:
    data = response.json()
    df = pd.json_normalize(data)
    print("Parsed as JSON ✅")
except Exception:
    try:
        # If not JSON, try CSV
        df = pd.read_csv(io.StringIO(response.text))
        print("Parsed as CSV ✅")
    except Exception as e:
        print("Could not parse response:", e)

# If DataFrame created, show only 10 rows
if df is not None:
    print(df.head(10))
else:
    print("No DataFrame created.")
