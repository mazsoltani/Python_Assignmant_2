
import random
while True:
    number_of_tas= random.randint(1 , 6)
    print("your Tas number is=" , number_of_tas)

    if number_of_tas == 6 :
        award= random.randint(1 , 6)
        print("your award is=" , award)
        break
    else:
        break