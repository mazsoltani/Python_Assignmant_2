hour = int(input("Please enter the hour= "))
minute = int(input("Pleaseenter minutes= "))
second = int(input("Please enter seconds= "))
if hour < 0 or minute< 0 or second < 0:
    print("Error...")
    
else:
    Time=hour*3600 + minute*60 + second

    print("Your Time is " ,Time,"Second")