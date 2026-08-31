credit_score = int(input("Enter credit score: "))
income = int(input("Enter monthly income: "))
liabilities = int(input("Enter existing liabilities: "))

if credit_score >= 750:
    credit_status = "eligible"
elif credit_score >= 650:
    credit_status = "conditional"
else:
    credit_status = "rejected"

income_status = income >= 50000
liability_status = liabilities <= 20000

if credit_status == "eligible" and income_status and liability_status:
    print("Loan Approved")

elif credit_status == "conditional" and income_status and liability_status:
    print("Loan Approved with Conditions")

else:
    print("Loan Rejected")