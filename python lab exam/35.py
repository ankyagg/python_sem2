def armstrong(num):
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        sum = sum + (d**3)
        temp = temp//10
    if sum==num:
        print("Armstrong no.")

    else:
        print("NOt")


num = int(input("ENter the no."))
armstrong(num)
