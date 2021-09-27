def square_digits(num):
    in_string = str(num)
    out_string = ''
    for s in in_string:
        out_string += str(int(s) ** 2)
    return int(out_string)


square_digits(9119)
