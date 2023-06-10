# TradingPatternScanner
![Python CI](https://github.com/white07S/TradingPatternScanner/actions/workflows/python-ci.yml/badge.svg)

#### Author: Preetam Sharma

Overview
--------

Trading Pattern Scanner Identifies complex patterns like head and shoulder, wedge and many more.

Installation / Usage
--------------------

Install using pip:

    $ pip install tradingpattern

    
# TradingPatternScanner

# Trading patterns:
* **Head and Shoulder and inverse Head and Shoulder**: These patterns indicate a potential reversal in the market, with the "head" being the highest point, and the "shoulders" being the points on either side at a slightly lower level.
* **Multiple top and bottom**: These patterns indicate a range-bound market, with multiple highs and lows forming a horizontal range.
* **Horizontal support and resistance**: These patterns indicate key levels at which the market has previously struggled to break through.
* **Ascending and Descending Triangle pattern**: These patterns indicate a potential breakout in the market, with the upper trendline being resistance and the lower trendline being support.
* **Wedge up and down**: These patterns indicate a potential reversal in the market, with the trendlines converging towards each other.
* **Channel up and down**: These patterns indicate a strong trend in the market, with price moving within a well-defined upper and lower trendline.
* **Double top and bottom**: These patterns indicate a potential reversal in the market, with the market hitting a high or low twice and then reversing.
* **Trend line support and resistance**: These patterns indicate key levels at which the market is likely to experience support or resistance based on historical price action.
* **Finding Higher-High and Lower-Low**

# Designed for fast performance:
* **Uses only Pandas as Numpy, no other external libraries**: This approach helps to keep the library lightweight and fast.
* **Uses the concept of vectorization**: This approach helps to improve performance by processing large amounts of data at once, rather than iterating over each individual data point.

# New and Unique:
* **No other python** library exists for such task currently: This library is new and unique, as it aims to provide an all-in-one solution for identifying various trading patterns.


### Lets check if its works for simplicity I used finviz and checked the pattern with the respective stock.

* Head and Shoulder:
![Head and Shoulder](https://user-images.githubusercontent.com/58583011/212490681-6dfca525-cd2e-4c87-830a-655ac9294a8a.png)

We can see that it finds out that we have inverse head and shoulder pattern in the stock on 9th Januray 2023 in 1 day interval. Lets match with Finviz.
![Finviz](https://user-images.githubusercontent.com/58583011/212490765-220182a5-e637-4f83-9a65-3031b7c99fee.png)

* We can see that Finviz also detects on 9th Januray 2023 in 1 day interval.
* You can adjust the window size to your liking. A smaller window size will be more sensitive to detecting patterns, but it will also increase the chances of false positives. A larger window size will be less sensitive to detecting patterns, but it will also decrease the chances of false positives.

# Future add-ons:
* **Request your favourite pattern to get added in the list**: The library is open for suggestions for adding new patterns.
* **Work on visualization and plotting**: The library can be extended to include visualization and plotting features to help users better understand the patterns identified.
* **Add unit testing**: The library can be extended to include unit testing to ensure that the code is working as expected and to catch any bugs early on.

