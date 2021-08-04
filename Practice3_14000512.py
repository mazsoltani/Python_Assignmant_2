
time=int(input("Please Enter Time in Second="))
if time<0:
    print("Eroor....Time Can not Negetive...")
else:
    hour=time // 3600
    minute=time-3600*hour
    minute=minute//60
    second=time - hour*3600 -minute*60

    print(hour,":",minute,":",second) 