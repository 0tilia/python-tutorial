
def max_num(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        return num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        return num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        return num3
    else:
        return num4

print(max_num(3, 50, 5, 100))


