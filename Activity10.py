input_tuple=tuple((input("Enter numbers separated by comma: ").split(",")))
for i in input_tuple:
    if(int(i)%5==0):
        print(i)
