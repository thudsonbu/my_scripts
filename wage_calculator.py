print("Enter an hourly wage")
wage = int(input())

print("Enter hours per week")
hours = int(input())

print("Weekly wage: " + str(wage*hours))
print("Monthly wage: " + str(wage*hours*4))
print("Yearly wage: " + str(wage*hours*52))