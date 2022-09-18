def make_operation(operator, *args):
    return_value = args[0]

    for number in args[1:]:
        if operator == "+":
            return_value += number
        elif operator == "-":
            return_value -= number
        elif operator == "*":
            return_value *= number
    return return_value