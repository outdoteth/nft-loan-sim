from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

returns = pd.read_csv("./expected_return.csv")
predicted_returns = pd.read_csv("./predicted_expected_return.csv")
put_returns = pd.read_csv("./put_expected_return.csv")

returns = returns.sort_values(by='x')
predicted_returns = predicted_returns.sort_values(by='x')
put_returns = put_returns.sort_values(by='x')

plt.plot(returns["x"], returns["y"], label="loan simulated (300,000 runs)")
# plt.plot(predicted_returns["x"], predicted_returns["y"], label="predicted value")
plt.plot(put_returns["x"], put_returns["y"], label="put simulated (300,000 runs)")

plt.axhline(y=35, color='r', linestyle='dashed', label="spot price")
plt.axhline(y=30, color='g', linestyle='dashed', label="loan/strike amount")

leg = plt.legend(loc='upper left')
plt.xlabel("coupoun/premium (ETH)")
plt.ylabel("value at end of term (ETH)")
plt.title("Expected value of 30 ETH loan/strike @ 10 ETH volatility, 35 ETH spot value")

plt.show()