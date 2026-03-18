
'''
Multi-Tiered Income Tax Calculation
Practice Problem: Calculate income tax for a given income based on these rules:
First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax
'''
tax1=0
tax2=0
tax3=0

salary=5000
if salary<10000:
    tax1=0
elif salary>10000 and salary<20000:
    tax2=(10/100)*(salary-10000)
else:
    remaining=salary-20000
    tax2=(10/100)*10000
    tax3=remaining*(20/100)
    
totaltax=tax1+tax2+tax3
print("TOTAL TAX: ",totaltax)
    