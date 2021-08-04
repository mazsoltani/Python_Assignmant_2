number = int(input("Please Enter a Number= "))

list_of_fibo = []

for i in range(number):

    if i == 0 or i == 1:
        list_of_fibo.append(1)
    
    else:
        fibo = list_of_fibo[i-1] + list_of_fibo[i-2]
        list_of_fibo.append(fibo)

print(list_of_fibo)