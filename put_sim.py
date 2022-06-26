from cmath import sqrt
from random import randrange
from numpy import random
import pandas as pd

def main():
    totals = {}
    start_price = 35
    volatility = 10
    strike = 30

    for i in range(0, 300_000):
        premium = (i % 200) * 0.1
        end_price = random.normal(start_price, volatility)
        payoff = min(strike, end_price) + premium

        premium_key = str(premium)

        if totals.get(premium_key) == None:
            totals[premium_key] = [0,0]

        totals[premium_key][0] += payoff
        totals[premium_key][1] += 1

    chart = {}
    for key, (total, count) in totals.items():
        chart[key] = total / count

    df = pd.DataFrame(chart.items(), columns=["x", "y"]).sort_values(by="x")
    df.to_csv("./put_expected_return.csv")

main()