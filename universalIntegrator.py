import math

location = str(input("Left, Middle, or Right?"))
equation = input("what is the equation?")
start = int(input("what is the starting x-value?"))
end = int(input("what is the final x-value?"))
partitions = int(input("how many partitions?"))

def riemann(location, equation, start, end, partitions):
    sum = 0
    width = abs((end - start) / partitions)
    for i in range(1, partitions + 1):
        if location == 'left':
            x = start + (end - start) * (i - 1) / partitions
            print(x)
        elif location == 'middle':
            x = start + (end - start) * (float(i) - 0.5) / partitions
            print(x)
        elif location == 'right':
            x = start + (end - start) * i / partitions
        y = eval(equation)
        sum += width * y
    print(sum)

riemann(location, equation, start, end, partitions)