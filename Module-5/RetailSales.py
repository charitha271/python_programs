import csv
import matplotlib.pyplot as plt

sales = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        amount = float(row["Sales"])

        sales[product] = sales.get(product, 0) + amount

print("\nRetail Sales Report")

for product, amount in sales.items():
    print(product, ":", amount)

products = list(sales.keys())
amounts = list(sales.values())

# Bar Chart
plt.bar(products, amounts, color="skyblue")

plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")

plt.show()

# Pie Chart
plt.pie(amounts, labels=products, autopct="%1.1f%%")

plt.title("Product Sales Distribution")

plt.show()