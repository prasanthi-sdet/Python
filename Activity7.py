list_input=input("Enter numbers separated by comma: ")
inputs=list_input.split(",")
result=0
for input_num in inputs:
    result+=int(input_num)
print(result)