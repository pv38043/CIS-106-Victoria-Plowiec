def compute_tuition(credit_hours,district_code):
    if district_code.upper() == "I":
        tuition = credit_hours * 250
    else:
        tuition = credit_hours * 550
    return tuition

total_tuition = 0
choice = input("Do you want to enter a student? (Yes or No): ")

while choice.lower() == "yes":
    last_name = input("Enter student last name: ")
    credit_hours = float(input("Enter credit hours: "))
    district_code = input("Enter district code (I or O): ")
    tuition = compute_tuition(credit_hours,district_code)

    print("Student:",last_name,)
    print("Tuition Owed:",tuition)

    total_tuition = total_tuition + tuition
    choice = input("Do you want to enter another student? (Yes or No): ")
print("Total Tuition for all students:",total_tuition)