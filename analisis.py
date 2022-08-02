import sys
import pandas as pd
from tools.tools import name_col, RSI, macd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle
import datetime
import numpy as np
from scipy.stats import linregress

# B is the rise percent of the candles next to the close of the last candle
#  that we use to decide if this sequence anticipate a rise


# in_ is the number of candles we consider to know if the price rises or fall
in_ = int(
    input(
        "Enter the number of candels (Y) to consider in the model for the prediction: \n"
    )
)
rows = int(
    input(
        "Enter the number of candels (X) consider in the model for the prediction: \n"
    )
)
periods = int(
    input("Enter the amount of periods for rsi calculation (14 recomended): \n")
)
p = rows + in_
temp = input("Enter the interval to consider, ex: 1d or 1h or 30m or 15m or 5m \n")

vol_p = int(input("Enter how many candels to consider if the market is ascending or descending: \n"))


def verify(file, vol_p=0):
    # create the index of the df
    index_ = name_col(rows)
    index_.append("date")
    index_.append("slope_prev")
    index_.append("slope_prev_short")
    index_.append("slope_next_short")
    index_.append("high")
    index_.append("low")
    index_.append("close")
    index_.append("mean_rel_15_30")
    index_.append("mean_rel_30_60")
    index_.append("mean_rel_60_100")
    k = pd.DataFrame(columns=index_)
    # Generate a list to analize the slope with linear regression from cero to rows
    X = [x for x in range(0, rows)]
    X_long = [x for x in range(0, vol_p)]
    X_next_short = [x for x in range(0, in_)]
    for i in range(p + vol_p, len(file.index)):
        Y = [file["close"][t] for t in range(i - p, i - in_)]
        Y_long = [file["close"][t] for t in range(i - vol_p - in_, i - in_)]
        Y_next_short = [file["close"][t] for t in range(i - in_, i)]
        slope_prev_short, intercept, r_value, p_value_2, std_err = linregress(X, Y)
        slope_prev, intercept, r_value, p_value_2, std_err = linregress(X_long, Y_long)
        slope_next_short, intercept, r_value, p_value_2, std_err = linregress(X_next_short, Y_next_short)
        vol = [file["volume"][i - x] for x in range(in_, p + 1 + vol_p)]
        vol_prom = np.mean(vol)
       # si_no = 1
        hi = np.max([(file["high"][i - t] - file["close"][i - in_]) / file["close"][i - in_] for t in range(in_ )])
        low = np.min([(file["low"][i - t] - file["close"][i - in_]) / file["close"][i - in_] for t in range(in_ )])
        close = np.mean([(file["close"][i - t] - file["close"][i - in_]) / file["close"][i - in_] for t in range(in_ )])
        mean_rel_15_30 = np.mean([file["close"][t] for t in range(i - 15-in_, i-in_)]) / np.mean([file["close"][t] for t in range(i - 30 - in_, i- in_)])
        mean_rel_30_60 = np.mean([file["close"][t] for t in range(i - 30-in_, i-in_)]) / np.mean([file["close"][t] for t in range(i - 60 - in_, i- in_)])
        mean_rel_60_100 = np.mean([file["close"][t] for t in range(i - 60-in_, i-in_)]) / np.mean([file["close"][t] for t in range(i - 100 - in_, i- in_)])
        # if the values in the row pass the filter, they are considered to make the predictor model
        # hi is the list with variaton of the candles we consider to know if the price rises or fall
        row = list()
        for t in range(in_, p + 1):
            row = row + [
                file["volume"][i - t] / float(vol_prom),
                (file["open"][i - t] - file["close"][i - t]) / file["low"][i - t],
                (file["close"][i - t] - file["open"][i - t]) / file["high"][i - t],
                (file["high"][i - t]) / (file["low"][i - t]),
                file["rsi"][i - t],
                file["macd"][i - t],
                file["macd_h"][i - t],
                file["macd_s"][i - t]
                ]

        row = row + [file["date"][i - in_],
                    slope_prev,
                    slope_prev_short,
                    slope_next_short,
                    hi,
                    low,
                    close,
                    mean_rel_15_30,
                    mean_rel_30_60,
                    mean_rel_60_100]
        k.loc[len(k.index)] = row
        k = k.dropna()
    return k


names = ["LISTA:"]
count = 0

for nam in range(1, len(sys.argv)):
    file = pd.read_csv(f"base/{str(sys.argv[nam])}_{temp}_base.csv")

    rsi = RSI(file["close"], periods)
    file["rsi"] = rsi
    file = macd(file)
    file.drop(index=file.index[:95], axis=0, inplace=True)
    file = file.reset_index()

    if count == 0:
        v = verify(file, vol_p)
        count += 1
    else:
        k = verify(file, vol_p)

        v = pd.concat([v, k], ignore_index=True)

    names.append(str(sys.argv[nam]))
st = str(datetime.datetime.now())
st = st.replace(" ", "_")
st = st.replace(":", "_")
v.to_excel(f"data/analysis_{st[0:16]}.xlsx", sheet_name="NUMBERS")
v.to_csv(f"analysis/analysis_{st[0:16]}.csv")