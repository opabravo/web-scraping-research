"""Split txt file into a xlsx file with custom format"""
from pathlib import Path
import pandas as pd
# 
BASE_PATH = Path(__file__).parent
TXT_FILE = BASE_PATH / "DomainUserV2.txt"


with open(TXT_FILE, "r", encoding="utf-16") as f:
    data = f.readlines()


# Transform data into xlsx file With columns: Email, Uid, Name, Company, Department, C1, C2, C3, C4, C5
data = [i.strip().split("\t") for i in data]
columns = ["C1", "Name", "Email", "Department", "Uid"]
df = pd.DataFrame(data, columns=columns)

# Add empty columns
df["Company"] = ""
df["C2"] = ""
df["C3"] = ""
df["C4"] = ""
df["C5"] = ""

# Reorder columns
df = df[["Email", "Uid", "Name", "Company", "Department", "C1", "C2", "C3", "C4", "C5"]]
df.to_excel("DomainUserV2.xlsx", index=False)
print("Done!")
