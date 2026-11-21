
import csv

# Read stocks from stocks.csv
stocks = {}

with open("stocks.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        stocks[row["Symbol"].upper()] = row

portfolio = {}

while True:
    print("\n===== INVESTMENT PORTFOLIO TRACKER =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ticker = input("Enter stock ticker: ").upper()

        if ticker in stocks:
            company = stocks[ticker]["Security"]
            sector = stocks[ticker]["GICS Sector"]

            print("Company:", company)
            print("Sector:", sector)

            buy_price = float(input("Enter buying price: "))
            quantity = int(input("Enter quantity: "))
            current_price = float(input("Enter current price: "))

            portfolio[ticker] = {
                "company": company,
                "sector": sector,
                "buy": buy_price,
                "quantity": quantity,
                "current": current_price
            }

            print("Stock added successfully!")

        else:
            print("Stock not found in stocks.csv!")

    elif choice == "2":
        total_investment = 0
        total_value = 0

        with open("portfolio_summary.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Ticker", "Company", "Quantity",
                "Buy Price", "Current Price",
                "Profit/Loss", "Gain/Loss %"
            ])

            for ticker, data in portfolio.items():
                investment = data["buy"] * data["quantity"]
                value = data["current"] * data["quantity"]
                profit = value - investment
                percentage = (profit / investment) * 100

                total_investment += investment
                total_value += value

                print("\nStock:", ticker)
                print("Company:", data["company"])
                print("Investment:", investment)
                print("Current Value:", value)
                print("Profit/Loss:", profit)
                print("Gain/Loss:", round(percentage, 2), "%")

                writer.writerow([
                    ticker, data["company"], data["quantity"],
                    data["buy"], data["current"],
                    profit, round(percentage, 2)
                ])

        print("\nTotal Investment:", total_investment)
        print("Total Portfolio Value:", total_value)
        print("Total Profit/Loss:", total_value - total_investment)
        print("Data saved successfully!")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
