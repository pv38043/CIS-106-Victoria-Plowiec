def compute_total(quantity, price):
    total = quantity * price

    if total > 10000:
        discount = total * 0.10
        total = total - discount
    return total

extended_price = 0
choice = input("Do you want to run this program? (Yes or No): ")

while choice.lower() == "yes":
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = compute_total(quantity, price)

    print("Quantity: ", quantity)
    print("Price: ", price)
    print("Total: ", total)

    extended_price = total + extended_price
    choice = input("Do you want to enter another? (Yes or No): ")
print("Extended price (sum of all totals): ", extended_price)