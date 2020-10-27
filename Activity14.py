def fibonacci(number):
    if number <= 1:
        return number
    else:
        return(fibonacci(number-1) + fibonacci(number-2))

nterms = int(input("Enter a Number: "))

if nterms <= 0:
    print("Please enter a valid positive number")
else:
    print("The output Fibonacci Sequence: ")
    for i in range(nterms):
        print(fibonacci(i))