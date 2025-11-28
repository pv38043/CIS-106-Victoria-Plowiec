def batting_average(hits, at_bats):
    average = hits / at_bats
    return average

player_count = 0
choice = input("Do you want to enter a player? (Yes or No): ")

while choice.lower() == "yes":
    last_name = input("Enter players last name: ")
    hits = float(input("Enter number of hits: "))
    at_bats = float(input("Enter number of at_bats: "))

    average = batting_average(hits, at_bats)

    print("Player:", last_name)
    print("Batting Average:", average)

    player_count = player_count + 1
    choice = input("Do you want to enter another player? (Yes or No): ")

print("Number of players entered:", player_count)