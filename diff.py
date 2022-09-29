
print('How many items do you wish to enter into the list?')
cnt = input()
input_array=list()
for i in range(1,int(cnt)+1):
    print('Please enter value #{} into the data list: '.format(str(i)))
    inpval = input()
    input_array.append(float(inpval))


difference_array = list()
for i in range(1,int(cnt)):
    difference = input_array[i]- input_array[i-1]
    difference_array.append(difference)


# find max value using loop
max_val = difference_array[0]
for val in difference_array:
    if val > max_val:
        max_val = val
# display the max value
print(max_val)


print('The highest difference between values is :' +  str(max_val))
