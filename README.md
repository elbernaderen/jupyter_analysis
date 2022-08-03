
# BTCUSDT_ADAUSDT_XMRUSDT_ETHUSDT_BNBUSDT_30m_hour_day.ipynb
This is the Jupyter Notebook that can be edited, and allow us to see if there exist a correlation in between the technical indicators, like:

    macd
    macd histogram
    macd signal
    RSI
    media
    
and the increments of the close values of the next candles. With this notebook, it is easy to interpretate the information using Pandas and Numpy, so then we can edit [amplitudes.py](https://github.com/elbernaderen/machine-learning-signal-finder#amplitudespy) following our results and results.
## Must install
[jupyter notebook](https://jupyter.org/install) and [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/install/) and [scipy](https://scipy.org/install/) libraries are used to work with data frames and lists. [sklearn](https://scikit-learn.org/stable/install.html) is a library used to create and train the machine learning model. [Seaborn](https://seaborn.pydata.org/) is used to make graphs.

# analysis.py
Edit a Crypto-currency Historical Data and add some technicals indicators so the Data can be analized with a jupyter notebook.

## Must install
[pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/install/) and [scipy](https://scipy.org/install/) libraries are used to work with data frames and lists. 




## Usage
Once we have downloaded the Cryptocurrency Historical Data (one or more) with the same interval in the same directory of the program, we call the program with the Crypto-currency  as command line arguments in capital letters as:

```bash
py amplitudes_rsi_vol_rsi.py BTCUSDT ETHUSDT ADAUSDT
```
Then, the program will ask the next variables:

```bash
Enter the number of candels (Y) to consider in the model for the prediction:
```
The increment before mentionated has to be between the Y candels
```bash
Enter the number of candels (X) considered in the model for the prediction:
```
These will be the candels we use to predict
```bash
Enter the amount of periods for rsi calculation (14 recomended):
```
A period for rsi calculation can be better for a candle interval analysis, and not for other one, so, it can be modificated if want it
```bash
Enter the interval to consider, ex: 1d or 1h or 30m or 15m or 5m 
```
The interval of the Crypto-currency Historical Data to consider.
```bash
Enter how many candels consider to calculate the volume mean:
```
To calculate the mean volume,so it can know if the volume has a increment or in other words if there are big participants, ex: 300.
Once the program have finished, a classification report will be printed in console, with the accuracy, precission, etc of the model, and a .csv file with all the historical data ready to use with the Jupyter Notebook.




# bina.py
## Description
This script contains **store_ohlcv** function, that is used to download the Crypto-currency Historical Data.
## Must install
[Binance](https://resilient-quant-trader.medium.com/scraping-crypto-currency-historical-data-from-binance-using-python-9c0e77c04df7) library to download Crypto-currency Historical Data and [pandas](https://pandas.pydata.org/) to work with data frames. 
Also need [yaml](https://pypi.org/project/PyYAML/) to save and read the api data in a yml file.
## Usage:
To use it, we need to have a Binance account. If you don't have one, can create a account following [this](https://www.binance.com/es/activity/referral-entry?fromActivityPage=true&ref=LIMIT_MYXYAGGF) and by doing that will be my refered and also colaborate with this project. Once that you have an account, you need to generate an API, as [follows](https://resilient-quant-trader.medium.com/scraping-crypto-currency-historical-data-from-binance-using-python-9c0e77c04df7). Then, have to set the API_key and the API_ secret in the config yml file located in the ignore folder.

# call_bina.py
Interface to download the Crypto-currency Historical Data to use them as base for [analysis.py](https://github.com/elbernaderen/jupyter_analysis/blob/main/README.md#analysispy) .
## Description
This script calls the function **store_ohlcv** from [bina.py](https://github.com/elbernaderen/machine-learning-signal-finder#binapy), that is used to download the Crypto-currency Historical Data, setting the name of the Crypto-currency in capital letters, name of the file that will be created, year, month and day since when take in count.
## Usage:
To download a Crypto-currency Historical Data for [amplitudes.py](https://github.com/elbernaderen/machine-learning-signal-finder#amplitudespy) and a Crypto-currency, for example ETHUSDT since a determinated date, must be called the program in console as continue:

```bash
py call_bina.py ETHUSDT base 2019 1 1
```
To download a Crypto-currency Historical Data for [analysis.py](https://github.com/elbernaderen/jupyter_analysis/blob/main/README.md#analysispy) and a Crypto-currency, for example  BTCUSDT since a determinated date, must be called the program in console as continue:
```bash
py call_bina.py BTCUSDT backtest 2022 3 5
```
# References:
* [Scraping Crypto-currency Historical Data from Binance using python](https://resilient-quant-trader.medium.com/scraping-crypto-currency-historical-data-from-binance-using-python-9c0e77c04df7)
* [RSI value](https://programmerclick.com/article/34731200625/) 
* [macd with PANDAS](https://www.alpharithms.com/calculate-macd-python-272222/)
# license:
MIT [Bernardo Derendinger](https://github.com/elbernaderen)
