# Aristocrats

"A company may be considered a dividend aristocrat if it raises its dividends consistently for at least the past 25 years."

This small software aim to go beyond that definition to identify the aristocrats-to-be by computing the dividend consistency over the years.

### Data Source

The first challenge was to find a datasource that we can rely on. The data used by the project has been extracted for a trial account from a website that will not be disclosed. Copying the data over your local machine is not legal.

But if you would like to move forward and get access to the full data for over 10,000 tickers, then feel free to contact the owner of the project.

### .env

In order to work, there must be a `.env` file at the root of the project with the following environment variables. Contact the owner of the project to get the proper values.

```sh
NETLOC=contact_maxime.rauer@gmail.com
COOKIE_NAME=contact_maxime.rauer@gmail.com
COOKIE_VALUE=ei873***************
COOKIE_FLAG=1
AWS_ACCESS_KEY_ID=AKIAU***************
AWS_SECRET_ACCESS_KEY=2ScW***************
BUCKET_NAME=aristocrats

```

### Data Output

The more recent data have been computed in December 2020. You can retrieve it at `data/aristocrats.csv`.

Columns definition:
* Ticker name (name of the stock).
* Last timestamp since trend have changed.
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
