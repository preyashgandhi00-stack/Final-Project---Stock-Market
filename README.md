# Final-Project---Stock-Market
#  Stock Data Analysis & Visualization Tool

---

##  Overview

This Python project is an **interactive command-line application** designed to analyze and visualize stock market data (specifically Airbnb or any user-provided dataset).

It enables users to:

* Load datasets dynamically
* Perform preprocessing and analysis
* Generate multiple financial visualizations
* Save charts for further use

The tool is beginner-friendly and demonstrates key concepts in **data analysis, financial metrics, and visualization**.

---

## Features

## Dataset Handling

* Choose between:

  * Default dataset (Airbnb stock data)
  * Custom CSV dataset
* Validates required columns (`Date`, `Close`, `Volume`)

###  Data Exploration

* View:

  * First 5 rows
  * Last 5 rows
  * Dataset structure (`info()`)
* Detect missing values

###  Data Processing

* Converts `Date` column to datetime format
* Sorts dataset chronologically
* Computes:

  * **20-day Moving Average (MA20)**
  * **50-day Moving Average (MA50)**
  * **Daily Returns**

###  Visualization Menu

Interactive menu-driven system:

1. Stock Price Trend
2. Volume Analysis
3. Correlation Heatmap
4. Daily Return Graph
5. Exit

###  Export Option

* Save any generated graph as a `.png` file

---

##  Libraries Used

| Library        | Purpose                                    |
| -------------- | ------------------------------------------ |
| **NumPy**      | Numerical operations                       |
| **Pandas**     | Data manipulation & analysis               |
| **Matplotlib** | Plotting graphs                            |
| **Seaborn**    | Advanced visualizations (heatmap, styling) |

---

##  Functions & Code Structure

###  `main()`

The core function that:

* Handles user input
* Loads dataset
* Performs preprocessing
* Displays menu and visualizations

###  Key Operations

* `pd.read_csv()` → Load dataset
* `df.head(), df.tail()` → Preview data
* `df.info()` → Dataset structure
* `pd.to_datetime()` → Convert dates
* `rolling().mean()` → Moving averages
* `pct_change()` → Daily returns
* `sns.heatmap()` → Correlation heatmap
* `plt.plot(), plt.bar()` → Graph plotting

---

## Project Use Cases

###  Financial Analysis

* Analyze stock trends and performance
* Identify moving averages and patterns

###  Learning Project

* Ideal for beginners learning:

  * Pandas
  * Data visualization
  * Time-series analysis

###  Data Exploration Tool

* Quickly explore any CSV dataset with time-series data

### Decision Support

* Helps visualize:

  * Price trends
  * Volatility (returns)
  * Trading volume

---

## Suggested Folder Structure

```
Stock-Analysis-Project/
│
├── data/
│   └── AIRBNB.csv
│
├── outputs/
│   └── (saved graphs)
│
├── src/
│   └── analysis.py
│
├── README.md
└── requirements.txt
```

---

##  Sample Output

###  Terminal Output

```
Dataset Menu:
1. Default Dataset
2. Use Your Own Dataset

Enter your choice: 1

First 5 rows of dataset:
        Date   Close   Volume
0 2022-01-01  150.23  1200000

Dataset info:
<class 'pandas.core.frame.DataFrame'>
...

Missing values:
Date      0
Close     0
Volume    0
```

---

###  Sample Graphs (Conceptual)

#### Stock Price Trend

* Line chart with:

  * Close Price
  * MA20
  * MA50

####  Volume Analysis

* Bar chart showing last 30 days volume

#### Correlation Heatmap

* Matrix showing correlation between variables

#### Daily Returns

* Line chart with fluctuations around zero

---

##  Author

**Preyash Gandhi**


