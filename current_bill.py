current bill
units = int(input("Enter the number of units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

if units >= 0:
    print("Total bill: Rs.", bill)