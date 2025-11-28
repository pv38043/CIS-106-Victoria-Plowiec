def get_rate(job_code):
    if job_code.upper() == "L":
        return 25
    elif job_code.upper() == "A":
        return 30
    elif job_code.upper() == "J":
        return 50
    else:
        return 0

total_gross = 0
choice = input("Do you want to enter an employee? (Yes or No): ")

while choice.upper() == "YES":
    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))
    rate = get_rate(job_code)

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate

    print("Employee:", last_name,)
    print("Hours Worked:", hours)
    print("Pay Rate:", rate)
    print("Gross Pay:", gross_pay)

    total_gross = total_gross + gross_pay

    choice = input("Do you want to enter another employee? (Yes or No): ")

print("Total Gross Pay for all employees:", total_gross)