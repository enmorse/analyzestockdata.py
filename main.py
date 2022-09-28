from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [
    1699.8,
    1777.44,
    2012.71,
    2003.0,
    1598.01,
    1690.17,
    1501.97,
    1718.73,
    1639.83,
    1780.75,
    1926.52,
    1775.07,
    1893.63
]

ebay_prices = [
    35.98,
    33.2,
    34.35,
    32.77,
    28.81,
    29.62,
    27.86,
    33.39,
    37.01,
    37.0,
    38.6,
    35.93,
    39.5
]


def get_returns(prices):
  returns = []

  for price in range(1, len(prices)-1):
    start_price = prices[price]
    end_price = prices[price + 1]
    returns.append(calculate_log_return(start_price, end_price))

  return returns


amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

display_x = [display_as_percentage(amazon_return)
             for amazon_return in amazon_returns]
display_y = [display_as_percentage(ebay_return)
             for ebay_return in ebay_returns]

print('The monthly returns for the Amazon stock are:', ', '
      .join(display_x),)
print('The monthly returns for the Ebay stock are:', ', '
      .join(display_y),)


calculate_x = calculate_variance(amazon_returns)
calculate_y = calculate_variance(ebay_returns)

# print(calculate_x)
# print(calculate_y)


std_dev_x = calculate_stddev(amazon_returns)
std_dev_y = calculate_stddev(ebay_returns)

display_stddev_x = display_as_percentage(std_dev_x)
display_stddev_y = display_as_percentage(std_dev_y)

# print(display_stddev_x)
# print(display_stddev_y)


cal_corr_x_y = calculate_correlation(amazon_returns,
                                     ebay_returns)

print("The correlation between the Amazon stock and "
      "the Ebay stock is:", cal_corr_x_y)
