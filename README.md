# Aristocrats

A company may be considered a dividend aristocrat if it raises its dividends consistently for at least the past 25 years.

This small software aim to go beyond that definition to identify the aristocrats-to-be buy computing the dividend increase consistency over any timeframe.

### Data Source

First of all, in order to compute the aristocrats, we needed a dataset of historical dividend.

Since more than 10,000 tickers data has been downloaded from a free account and we did not have the license to copy it over, please contact the owner of the project if you'd like to get some information about how to source the data on your own.

### .env

If you would like to download some recent data, you would have to create a `.env` file at the root of the project with the following keys. To get the value, feel free to reach the owner of the project.

```sh
NETLOC=the_website_source.com
COOKIE_NAME=cookie_name
COOKIE_VALUE=cookie_value
COOKIE_FLAG=1
AWS_ACCESS_KEY_ID=AKIAU***************
AWS_SECRET_ACCESS_KEY=2ScW***********************
BUCKET_NAME=aristocrats

```

### Data Output

The more recent public dataset has been computed in December 2020 and is located at `data/aristocrats.csv`.

Columns legend is:
* Ticker name (name of the stock).
* Last timestamp since a dividend 
* Rounded number of years in a row the dividend payout has been increasing.
* Dividend category (from `regular` to `aristocrat`)

### Commands

If you would like to use this tool or contribute to it, you'll need `Docker` and `make` installed. The `.env` file is required.

Those are all the available commands:

```sh
make build (build the Docker image)
make run (run the project, you will enter a terminal)
make grab source tickers (get the full list of tickers)
make grab source dividends (get the dividend data for each ticker)
make convert (extract the data we need from the dataset)
make compute (compute the dividends)
make save (store datasets to S3)
make load (load datasets from S3)
```
