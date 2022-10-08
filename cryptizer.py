# Importing the required modules
import requests
import re

version = '1.0.0' # DO NOT CHANGE

# Defining the version checker function
def updater():

    # Getting data from github
    response = str(requests.get("https://raw.githubusercontent.com/LeoBlox5128/cryptizer/main/README.md").content)

    # Searching for latest version in README.md
    x = re.search(r"""version: (.*) --\\n""", response)

    # Converting latest version to a string
    xconverted = x[1]

    # Warning the user about it
    if xconverted != version:
        print("You are using an outdated version of Cryptizer! Please install the latest version from GitHub to continue, as this version may be potentionally unsafe!")
        exit()

# Running the updater function.
updater()

# Defining the main function
def main():

    # Getting user input and variables
    try:
        currency = str(input("Enter full cryptocurrency token name > "))
    except KeyboardInterrupt:
        print("Cancelled")
        exit()
    url = f'https://coinmarketcap.com/currencies/{currency}/'

    # Getting data from website, then searching for price in site source code
    response = str(requests.get(url).content)
    x = re.search(r"""price":(.*),"priceCu""", response)

    # Checking if the currency exists
    if x == None:
        print("That cryptocurrency token either doesn't exist or you've spelt it wrong! (CTRL+C to cancel)")
        main()
    else:

        # Getting the number from dictionary, converting it to a float and rounding it
        xconverted = x[1]
        floated = float(xconverted)
        rounded = round(floated, 2)

        # Printing the price
        print(f"1 {currency.capitalize()} --> {rounded}$")

# Running the main function
main()



