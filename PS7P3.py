def trip_info(miles,gallons):
    mpg = miles / gallons
    gas_cost = gallons * 3.00
    return mpg, gas_cost

trip_count = 0
total_miles = 0
total_gas_cost = 0

choice = input("Do you want to enter a trip? (Yes or No): ")

while choice.lower() == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg, gas_cost = trip_info(miles,gallons)

    print("City:", city)
    print("Miles:", miles)
    print("Miles per gallon (MPG):", mpg)
    print("Gas cost:", gas_cost)

    trip_count = trip_count + 1
    total_miles = total_miles + miles
    total_gas_cost = total_gas_cost + gas_cost

    choice = input("Do you want to enter another trip? (Yes or No): ")
print("Number of trips entered:",trip_count)
print("Total miles traveled:",total_miles)
print("Total gas cost for all trips:",total_gas_cost)