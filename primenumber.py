#Prime number
def prime(lim):
    primelist = []
    for num in range(1,lim):
        if num>1:
            for i in range(2,num):
                if(num%i ==0):
                    break
            else:
                primelist.append(num)

    return primelist 

lim = int(input("To how many number you want to generate prime number list: "))
print(prime(lim))