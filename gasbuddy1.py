print("How many gas stations will you store?")
num_input = int(input())
loop_variable = 1
input_array=list()
while loop_variable<=num_input:
    print("What is the gas price at station #" + str(loop_variable))
    inp=int(input())
    input_array.append(inp)
    loop_variable=loop_variable+1

min_val=input_array[0] #assinging the first value to the variable before looping to find if there are any lower values
index=0
index_out=1
for i in input_array:
    index = index + 1
    if i < min_val:
        min_val = i
        index_out=index # storing the index of the item which matched the lowest item






print("The lowest price of gas found was station #{} at ${}".format(str(index_out),str(min_val))  )
