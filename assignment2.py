print('How many items do you wish to enter into the list?')
numofinput=input()
inputarray=list()
for i in range(0,int(numofinput)):
    print('Please enter value #{} into the list'.format(str(i)))
    inp=input()
    inputarray.append(int(inp))

cnt=0
for j in inputarray:
    cnt=cnt+1
    if j>=0:
        print('Value #{} [{}] is positive'.format(str(cnt),str(j)))
    else:
        print('Value #{} [{}] is negative'.format(str(cnt),str(j)))

test