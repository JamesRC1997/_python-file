# input statements
salary = float(input())
numDependents = int(input())

# Constants for tax rates and deductions
statetaxrate = 0.065
federaltaxrate = 0.28
dependentdeductionrate = 0.025

# calculate taxes here
stateTax = salary * statetaxrate
federalTax = salary * federaltaxrate

# Calculate dependent deductions
dependentDeduction = salary * dependentdeductionrate * numDependents

# Calculate total withholding
totalWithholding = stateTax + federalTax + dependentDeduction

# Calculate take-home pay
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependent: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))