import datetime, csv, json

path = 'data/btcusd_1-min_data.csv'

#order = timestamp
def read_data(path):
   with open(path, 'r') as file:
    next(file)
    csv_file = csv.reader(file)
    for row in csv_file:
        timestamp = float(row[0])
        open = float(row[1])
        hig = float(row[1])
        low = float(row[1])
        close = float(row[1])
        volume = float(row[1])


def check_5_min(count):
    if count % 5 == 0:
       return True
    else:
       return False
    

def load_api_key():
   with open("env.json", "r") as file:
      data = json.load(file)
      api_key = data["api_key"]

