
# cand avem eroare de division + de
try:
    value = 10/0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")

# best practice pt error
try:
    answer = 10/0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")



