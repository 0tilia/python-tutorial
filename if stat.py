
you_love_me = True

if you_love_me:
    print("Me happy")
else:
    print("Me not happy")


is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")

elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")


