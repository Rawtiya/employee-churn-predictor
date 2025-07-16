
def clean(data):
    return [row for row in data if row['Age'] and row['Tenure']]

if __name__ == "__main__":
    from read_data import read_csv
    raw = read_csv("data/raw_data.csv")
    cleaned = clean(raw)
    print(cleaned)
