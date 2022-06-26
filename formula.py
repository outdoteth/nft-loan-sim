import scipy.integrate as integrate
import math
import pandas as pd

def b(z, vol, spot):
    print("vol", vol, spot, z)
    return z * (1/(vol * math.sqrt(2 * math.pi))) * (math.e ** (-0.5 * (((z-spot) / vol) ** 2)))

def p(vol, spot, loan, coupon):
    return 0.5 * (1 + math.erf((loan + coupon - spot) / (vol * math.sqrt(2))))

def main():
    chart = {}

    for i in range(0, 200):
        coupon = i * 0.1
        loan = 30
        vol = 10
        spot = 35

        _b = integrate.quad(b, 0, loan + coupon, args=(vol, spot))[0]
        _p = p(vol, spot, loan, coupon)
        _a = (loan + coupon) * (1 - _p)
        _y = _b + _a;

        print("running", _b, _p, _a, _y)

        chart[coupon] = _y

    df = pd.DataFrame(chart.items(), columns=["x", "y"]).sort_values(by="x")
    df.to_csv("./predicted_expected_return.csv")

main()