import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

returns = pd.read_csv("./expected_return.csv")

returns = returns.sort_values(by='x')

plt.plot(returns["x"], returns["y"])

plt.xlabel("coupoun (ETH)")
plt.ylabel("expected value (ETH)")
plt.title("Expected value with respective coupon payments at expiration of a 30 ETH loan for asset with 35 ETH spot price and 5 ETH volatility")

plt.show()