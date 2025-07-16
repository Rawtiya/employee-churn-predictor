
import csv

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

if __name__ == "__main__":
    data = read_csv("data/raw_data.csv")
    print(data)
