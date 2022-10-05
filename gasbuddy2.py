
input_array=list()
loop_variable=0
inp=0
exit_flag= False
while exit_flag==False:
    loop_variable=loop_variable+1
    print("What is the gas price at station #" + str(loop_variable))
    inp=input()
    if str(inp).upper() == "QUIT":
        exit_flag = True
    else:
        input_array.append(int(inp))
        

min_val=input_array[0]#assinging the first value to the variable before looping to find if there are any lower values
max_val= input_array[0] #assinging the first value to the variable before looping to find if there are any lower values
index=0
index_min_out=1
index_max_out=1
sum_of_array=0
for i in input_array:
    sum_of_array=sum_of_array+i
    index = index + 1
    if i < min_val:
        min_val = i
        index_min_out=index # storing the index of the item which matched the lowest item
    if i> max_val:
        max_val=i
        index_max_out=index


average= sum_of_array/index

print("The highest price of gas found was station #{} at ${}".format(str(index_max_out),str(max_val))  )
print("The average gas price was $" + str(average))
print("The lowest price of gas found was station #{} at ${}".format(str(index_min_out),str(min_val))  )
