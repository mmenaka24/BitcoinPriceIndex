import sys
import requests


def main():
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
    except requests.RequestException:
        sys.exit("Sorry, could not access bitcoin price")

    response = r.json()
    try:
        return float(response["data"]["priceUsd"])
    except (ValueError, KeyError) as e:
        # print(response)
        sys.exit("Sorry, unknown bitcoin price")


if __name__ == "__main__":
    main()
