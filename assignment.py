Assignment 1

inputarray=list()
for i in range(1,7):
    inp = input()
    inputarray.append(int(inp))

print(inputarray)
print("Please enter a number to check the frequency")

inp2=int(input())

frequency =0
for num in inputarray:
    if inp2==num :
        frequency = frequency+1

print('We found {} value(s) of {} within the data list given'.format(str(inp2),str(frequency)))


