print("Do you want to enter data(yes or no)")
response = input()
while response == "yes":
    print("Enter last name")
    lastname = input()
    print("Enter hours worked")
    hw = float(input())
    print("Enter rate of pay")
    rateofpay = float(input())
    grosspay = hw * rateofpay
    print("employee name: " + lastname + " grosspay: " + str(grosspay))
    print("Do you wanna enter another employee (yes or no)")
    response = input()
