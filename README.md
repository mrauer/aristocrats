<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/mrauer/aristocrats">
    <img src="images/logo.png" alt="Logo">
  </a>

  <h3 align="center">Aristocrats</h3>

  <p align="center">
    Identification of prospective aristocrat stocks.
    <br />
    <br />
    <a href="https://github.com/mrauer/aristocrats/issues">Report Bug</a>
    ·
    <a href="https://github.com/mrauer/aristocrats/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#data-source">Data Source</a></li>
    <li><a href="#env">.env</a></li>
    <li><a href="#data-output">Data Output</a></li>
    <li><a href="#commands">Commands</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

"A company may be considered a dividend aristocrat if it raises its dividends consistently for at least the past 25 years."

This small software aim to go beyond that definition to identify the `aristocrats-to-be` by computing the dividend consistency over the years.

<!-- DATA SOURCE -->
## Data Source

The first challenge was to find a datasource that we can rely on. The data used by the project has been extracted from a trial account of a company that will not be disclosed: copying the data without license over your local machine is not legal.

But if you would like to move forward and get access to the full data history of over 10,000 tickers, then feel free to contact the owner of the project.

<!-- ENV -->
## .env

In order to work, you must placed an `.env` file at the root of the project with the following environment variables. Contact the owner of the project to get the proper values.

```sh
NETLOC=contact_maxime.rauer@gmail.com
COOKIE_NAME=contact_maxime.rauer@gmail.com
COOKIE_VALUE=ei873***************
COOKIE_FLAG=1
AWS_ACCESS_KEY_ID=AKIAU***************
AWS_SECRET_ACCESS_KEY=2ScW***************
BUCKET_NAME=aristocrats

```

<!-- DATA OUTPUT -->
## Data Output

The more recent data have been computed in December 2020. You can retrieve it at `data/aristocrats.csv`.

Columns definition:
* Ticker name (name of the stock).
* Last timestamp since trend have changed.
* Rounded number of years in a row the dividend payout has been increasing.
* Dividend category (from `regular` to `aristocrat`)

<!-- COMMANDS -->
## Commands

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

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
