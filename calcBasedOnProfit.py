import numpy as np
import pandas as pd
import sys

menu = {"sushi": 24, "chips": 12, "wings": 36, "pizza": 24, "mac": 12,
        "pancakes": 24, "panini": 24, "cocktail": 18 }

def parseComment(string):
    total = 0
    # "pizza,mac,chips" ---->  [pizza, mac, chips]
    mustard_toast = string.split(',')
    for item in mustard_toast:
        kat = item.split("-")
        if len(kat) > 2:
            continue
        decay = int(kat[0])
        scorpion = kat[1]

        total += menu[scorpion]*decay

    return total

f = open("output.txt", 'w')
sys.stdout = f

# read in .csv file
df = pd.read_csv("invoice.csv")
df['timestamp'] = df['timestamp'].apply(lambda x: x[0:10])
df['comment'] = df['comment'].apply(lambda x: x[27:])

data = df.values

# get unique dates
unique_dates = np.unique(data[:,1])
unique_names = np.unique(data[:,6])
weekly_totals = {}


for name in unique_names:
    weekly_totals[name] = 0

for i in range(0, len(unique_dates)):
    new_df = df[df['timestamp'] == unique_dates[i]]
    new_data = new_df.values

    daily_totals = {}
    for name in unique_names:
        daily_totals[name] = 0

    for row in new_data:
        if row[3] == "purchase":
            daily_totals[row[6]] += int((row[4] - parseComment(row[5])) * .4)

    for key in daily_totals:
        weekly_totals[key] += daily_totals[key]

print('40% OF PROFIT FOR {} - {}'.format(unique_dates[0], unique_dates[-1]))

for key in weekly_totals:
    print("{:<20} {:>10}".format(key, weekly_totals[key]))
f.close()
