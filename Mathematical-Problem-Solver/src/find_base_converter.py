def decimal_to_base(number, base):
    if number == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base

    return result


def base_to_decimal(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = number.upper()

    result = 0

    for digit in number:
        value = digits.index(digit)
        result = result * base + value

    return result


def base_a_to_base_b(number, base_a, base_b):
    decimal_value = base_to_decimal(number, base_a)
    return decimal_to_base(decimal_value, base_b)