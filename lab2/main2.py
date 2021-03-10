import numbers

# Definition of test cases
DICTIONARY_1 = {"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}
DICTIONARY_2 = {"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}
DICTIONARY_3 = {"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}
DICTIONARY_4 = {"cost_price": 5.50, "sell_price": 9.00, "inventory": 200}
DICTIONARY_5 = {"cost_price": 20.12, "sell_price": 43.20, "inventory": 150}
DICTIONARY_6 = {"cost_price": 15.00, "sell_price": 18.40, "inventory": 200}
DICTIONARY_7 = {"cost_price": 26.00, "sell_price": 35.00, "inventory": 75}
DICTIONARY_8 = {"cost_price": 110.20, "sell_price": 140.50, "inventory": 960}
DICTIONARY_9 = {"cost_price": 16.45, "sell_price": 17.95, "inventory": 800}
DICTIONARY_10 = {"cost_price": "11", "sell_price": 15.93, "inventory": 50}

TEST_CASES = [DICTIONARY_1, DICTIONARY_2, DICTIONARY_3, DICTIONARY_4, DICTIONARY_5,
DICTIONARY_6, DICTIONARY_7, DICTIONARY_8, DICTIONARY_9, DICTIONARY_10]

def calculate_profit(properties):
    # Validate the properties
    assert(isinstance(properties["cost_price"], numbers.Number))
    assert(isinstance(properties["sell_price"], numbers.Number))
    assert(isinstance(properties["inventory"], numbers.Number))

    total_cost = properties["cost_price"] * properties["inventory"]
    total_sales = properties["sell_price"] * properties["inventory"]

    return round(total_sales - total_cost)

for dictionary in TEST_CASES:
    try:
        profit = calculate_profit(dictionary)
        print(profit)
    except AssertionError:
        print("Invalid parameters")