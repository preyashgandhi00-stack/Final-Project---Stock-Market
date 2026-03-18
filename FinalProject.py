import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    print("\nDataset Menu:")
    print("1. Default Dataset")
    print("2. Use Your Own Dataset")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    match choice:
        case 1:
            df = pd.read_csv("F:/Python/AIRBNB.csv")
        case 2:
            path = input("Enter your dataset CSV path: ")
            df = pd.read_csv(path)
        case _:
            print("Invalid choice")
            return

    print("\nFirst 5 rows of dataset:")
    print(df.head())

    print("\nLast 5 rows of dataset:")
    print(df.tail())

    print("\nDataset info:")
    print(df.info())

    required_columns = ['Date', 'Close', 'Volume']
    for col in required_columns:
        if col not in df.columns:
            print(f"Error: Required column '{col}' not found in dataset.")
            return

    print("\nConvert Date column:")
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df.sort_values('Date')

    print("\nMissing values:")
    print(df.isnull().sum())

    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['Daily Return'] = df['Close'].pct_change()

    while True:
        print("\nVisualization Menu")
        print("1. Stock Price Trend")
        print("2. Volume Analysis")
        print("3. Correlation Heatmap")
        print("4. Daily Return Graph")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                fig = plt.figure(figsize=(16, 7))
                plt.plot(df['Date'], df['Close'], label="Close Price", color="royalblue", linewidth=2.5)
                plt.plot(df['Date'], df['MA20'], label="20 Day MA", color="orange", linestyle="--", linewidth=2)
                plt.plot(df['Date'], df['MA50'], label="50 Day MA", color="green", linestyle="--", linewidth=2)
                plt.fill_between(df['Date'], df['Close'], df['MA20'], color="blue", alpha=0.1)
                plt.title("AirBNB Price Trend")
                plt.xlabel("Date")
                plt.ylabel("Price")
                plt.legend(loc="upper left", fontsize=10)
                plt.grid(True, linestyle="--", alpha=0.6, color="gray")
                plt.tight_layout()
                plt.show()

                save = input("Save graph? (yes/no): ")
                match save.lower():
                    case "yes":
                        name = input("\nEnter file name: ")
                        fig.savefig(name + ".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            case 2:
                sns.set_style("darkgrid")
                fig = plt.figure(figsize=(16, 6))
                plt.bar(df['Date'].tail(30), df['Volume'].tail(30),
                        color="steelblue", edgecolor="black", label="Trading Volume", alpha=0.8)
                plt.title("AirBNB - Last 30 Days Trading Volume", fontsize=15, fontweight="bold")
                plt.xlabel("Date", fontsize=12)
                plt.ylabel("Volume Traded", fontsize=12)
                plt.xticks(rotation=45)
                plt.grid(axis='y', linestyle="--", alpha=0.6)
                plt.tight_layout()
                plt.legend()
                plt.show()

                save = input("Save graph? (yes/no): ")
                match save.lower():
                    case "yes":
                        name = input("\nEnter file name: ")
                        fig.savefig(name + ".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            case 3:
                sns.set_style("dark")
                fig = plt.figure(figsize=(10, 7))
                sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm",
                            linewidths=0.5, linecolor="white", fmt=".2f", cbar=True)
                plt.title("AirBNB - Stock Data Correlation")
                plt.xticks(rotation=0)
                plt.yticks(rotation=0)
                plt.tight_layout()
                plt.show()

                save = input("Save graph? (yes/no): ")
                match save.lower():
                    case "yes":
                        name = input("\nEnter file name: ")
                        fig.savefig(name + ".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            case 4:
                fig = plt.figure(figsize=(14, 6))
                plt.plot(df['Date'], df['Daily Return'], color="royalblue",
                         linewidth=2, marker="o", markersize=4, label="Daily Return")
                plt.axhline(0, color="crimson", linestyle="--", linewidth=1)
                plt.title("AirBNB - Daily Return of Stock")
                plt.xlabel("Date", fontsize=12)
                plt.ylabel("Return", fontsize=12)
                plt.xticks(rotation=0)
                plt.grid(True, linestyle="--", alpha=0.6)
                plt.legend()
                plt.tight_layout()
                plt.show()

                save = input("Save graph? (yes/no): ")
                match save.lower():
                    case "yes":
                        name = input("\nEnter file name: ")
                        fig.savefig(name + ".png")
                    case "no":
                        pass
                    case _:
                        print("Invalid option")

            case 5:
                print("Analysis Completed")
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()