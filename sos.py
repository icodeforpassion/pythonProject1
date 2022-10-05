exit_flag=True
while exit_flag != False:
    print("What number should we determine")
    input_num=input()
    if int(input_num) == -1:
        print("Thank you. Program over!")

        exit_flag = False
    elif int(input_num) <=0:
        print("Invalid input. Please enter a value > 1")
    else:
        sos = 0  # initialising the output variable
        for i in range(1,int(input_num)+1):
            sos = sos + (i** 2)

        print("The sum of squares for 4 is " + str(sos))
