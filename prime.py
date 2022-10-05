print("What value are we looking for primes?")

inp=int(input())

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

reminder = 0
primefactors= list()

continueloop = True
while continueloop == True:

    initnum = inp
    loopcount =0
    for primenum in prime_numbers:
        reminder=0

        while reminder==0:
            loopcount += 1
            if loopcount==1:
                nextnum = initnum
            else:
                nextnum=divided_inp
            reminder =  nextnum % primenum
            if reminder==0:
                continueloop = True
                primefactors.append(primenum)
                divided_inp=nextnum / primenum
            else:
                divided_inp=nextnum
                continueloop= False



print("The prime factors for {} are: ".format(str(inp)))
print(primefactors)
