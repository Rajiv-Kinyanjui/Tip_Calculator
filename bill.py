print("We hope you have enjoyed our food and the service. Kindly enter your total bill so as to receive the total amount to pay")

bill = int(input())

print("Kindly tell us whether the service was good or great or terrible")


service = input()

if service == "good":
    tip = 0.15 * bill
    total = bill + tip
    print(total)

elif service == great":
    tip = 0.2 * bill
    total = bill + tip
    print(total)

else:
    print(bill)