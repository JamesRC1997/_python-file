#declared variables
Employeename = "Jenna Jenkins"
NumofShifts = 15
NumofTran = 30
TranDollarVa = 25000
#productivity calculation
ProductScore = (TranDollarVa / NumofTran) / NumofShifts
#Productivity Bonus
if ProductScore <= 30:
    EmployeeBonus = 50.00
elif ProductScore <= 69:
    EmployeeBonus = 75.00
elif ProductScore <= 199:
    EmployeeBonus = 100.00
else: EmployeeBonus = 200
# Output Name and Bonus
print ("Employee Name:" + str(Employeename))
print ("Employee Bonus:$" + str(EmployeeBonus))