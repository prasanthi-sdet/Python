list_input=list(input("Enter numbers separated by comma: ").split(","))
if(int(list_input[0])==int(list_input[-1])):
    print("Is the first and last numbers in list are same? TRUE")
else:    
    print("Is the first and last numbers in list are same? FALSE")