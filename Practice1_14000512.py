sum = 0
print("If You Want to Exit Please Type exit ")
while True :

    num = input("Please Enter a Number= ")
    
    if num == "exit":
       
        break

    sum = float(num)+sum
print("Summation is=",sum)
