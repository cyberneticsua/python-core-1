def fizz_buzz(param):
    if param % 3 == 0 and param % 5 != 0:
        return "fizz"
    elif param % 3 != 0 and param % 5 == 0:
        return "buzz"
    elif param % 3 == 0 and param % 5 == 0:
        return "fizzbuzz"
    else:
        return param

