import sys
import requests


def main():
    # Get the number of Bitcoins from the user
    bitcoin_nos = bitcoin_no()

    # Fetch the current price of one Bitcoin
    amount = bitcoin_price()

    # Calculate total value and print it formatted to 4 decimal places with commas
    amount = amount * bitcoin_nos
    print(f"${amount:,.4f}")


def bitcoin_no():
    try:
        # Check if the user provided exactly one command-line argument
        if len(sys.argv) == 2:
            no_of_bitcoin = float(sys.argv[1])
            return no_of_bitcoin

        else:
            sys.exit("Missing command-line argument")

    # Handle cases where the input string cannot be converted to a float
    except ValueError:
        sys.exit("Command-line argument is not a number")


def bitcoin_price():
    try:
        # Request Bitcoin data from the CoinCap API
        bitcoin_info = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=27ac7e8e5ed9e386f0792b8b33de8d99b89699d636fb7a09b3980bf66c6847b2")

        # Parse the JSON response and extract the current USD price
        response = bitcoin_info.json()
        bitcoin_price = float(response['data']['priceUsd'])
        return bitcoin_price

    # Gracefully exit if there is a network connection or API error
    except requests.RequestException:
        sys.exit("Network error")


main()
