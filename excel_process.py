"""Split txt file into a xlsx file with custom format"""
from pathlib import Path
import pandas as pd


BASE_PATH = Path(__file__).parent
CSV_FILE = BASE_PATH / "DomainUser-sample.csv"


def process_csv(csv_file: Path):
    df = pd.read_csv(csv_file, encoding="utf-16")
    output_df = pd.DataFrame(columns=["Email", "Uid", "Name", "Company", "Department", "C1", "C2", "C3", "C4", "C5"])

    # Loop through each row
    for _, row in df.iterrows():
        data_lst = row[0].split()
        try:
            row_output = {
                "C1": data_lst[0],
                "Name": data_lst[1],
                "Email": data_lst[2],
                "Department": "".join(data_lst[3:-1]),
                "Uid": data_lst[-1],
            }
            output_df = pd.concat([output_df, pd.DataFrame([row_output])], ignore_index=True)
        except IndexError:
            print("Skipiping:")
            print(data_lst)
            continue

    output_df.to_excel("DomainUserV2.xlsx", index=False)
    print("Done!")


if __name__ == "__main__":
    process_csv(CSV_FILE)
