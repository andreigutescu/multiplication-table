from random import randrange

while True:
    number1 = randrange(1,10)
    number2 = randrange(1,10)
    expected_result = number1 * number2

    user_result = int(input(f"{number1} * {number2} = "))

    if user_result == expected_result:
        print("correct")
    else:
        print("wrong")
    while user_result != expected_result:
        print("wrong, try again")
        user_result = int(input(f"{number1} * {number2} = "))