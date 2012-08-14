import sys
import csv

def sc_dict(row):
    return dict(year = row[0], champions = row[1])

def cleanup_years(d):
    year = d['year'].split("-")[0]
    year = int(year) + 1
    return dict(year = str(year), champions = d['champions'])

def custom_index(array, compare_function, k):
    for i, v in enumerate(array):
        if compare_function(v, k):
            return i
    return -1

def compare_year(a, b):
    return a['year'] == b

def find_winner(winners, year):
    index =  custom_index(winners, compare_year, year)
    if index == -1:
        return None
    else:
        return winners[index]

sc_winners = []
league_winners = []
with open("england.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
         league_winners.append(row)

with open("charity_shield.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
         sc_winners.append(row)


sc_winners = map(sc_dict, sc_winners)[1:]
league_winners = map(sc_dict, league_winners)[1:]
league_winners = map(cleanup_years, league_winners)

for w in sc_winners:
    lw = find_winner(league_winners, w['year'])
    w['league_winner'] = lw['champions']

unique_scs = []
for w in sc_winners:
    if w['champions'] not in unique_scs:
        unique_scs.append(w['champions'])

print unique_scs
