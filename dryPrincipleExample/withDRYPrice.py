# Function to calculate total price with tax
def calculate_total_price(price, tax_rate):
    return price + (price * tax_rate)

# Items and tax rate
tax_rate = 0.15
prices = [100, 200, 50]

# Initialize item counter
item_number = 1

# Calculate and display total price for each item
for price in prices:
    total_price = calculate_total_price(price, tax_rate)
    print(f"Total price for item {item_number}: {total_price}")
    item_number += 1
