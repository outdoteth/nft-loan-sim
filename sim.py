# set a constant loan amount
from cmath import sqrt
from random import randrange
from numpy import random
import pandas as pd


def main():
    totals = {}
    loan = 31.74

    for i in range(0, 10_000_000):
        coupoun = randrange(-10, 200) / 10
        start_price = 35
        end_price = random.normal(start_price, 5)
        payoff = min(coupoun + loan, end_price)

        coupoun_key = str(coupoun)

        if totals.get(coupoun_key) == None:
            totals[coupoun_key] = [0,0]

        totals[coupoun_key][0] += payoff
        totals[coupoun_key][1] += 1

    chart = {}
    for key, (total, count) in totals.items():
        chart[key] = total / count

    df = pd.DataFrame(chart.items(), columns=["x", "y"]).sort_values(by="x")
    df.to_csv("./expected_return.csv")



# for:
# pick a random coupoun payment (x)
# sample a random variable price from normal distribution of sigma, mean
# get the payoff min(coupoun+loan, price) (y)
# totals[x] += y
# counts[x] += 1
# for each total:
#   avg = total / count
#   chart[x] = avg

main()