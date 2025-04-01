import sys
import requests


def main():

    # Calculates and prints the total cost of purchasing n Bitcoins
    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = get_bitcoin_price()
    purchase_price = n * price

    print(f"${purchase_price:,.4f}")


def get_bitcoin_price():
    try:
        r = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        # This version of the API is being discontinued. Can update to v3 of the API at https://pro.coincap.io/dashboard
        # New API link is rest.coincap.io/v3/assets, but need a bearer token to access

        r.raise_for_status()  # Raises an HTTPError for non-200 responses, which is then caught by the line below (otherwise RequestException would only catch connection issues)

    except (
        requests.RequestException
    ) as e:  # the exception object is assigned to a variable e

        sys.exit(f"Error fetching Bitcoin price: {e}")

        # If the request fails, the error message will be displayed to help with debugging

    response = r.json()
    try:
        return float(response["data"]["priceUsd"])
    except (
        ValueError,
        KeyError,
    ):  # Don't need 'as e' if error message is not being used
        # print(response)
        sys.exit("Unexpected API response format")


if __name__ == "__main__":
    main()
