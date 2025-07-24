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

def run_base_converter():
    number = input("Enter the number to convert (accepts any base): ")
    baseIn = int(input("Enter the inputted base (decimal is base 10): "))
    baseOut = int(input("Input the base you want to output: "))
    result = decimal_to_base(int(number, baseIn), baseOut)
    return result