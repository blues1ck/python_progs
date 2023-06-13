input_str = input().split()

result_dict = {}

for complex_num in input_str:
    if '-' in complex_num:
        real_part, imag_part = map(float, complex_num.split('-'))
        imag_part = '-' + imag_part[:-1]
    elif '+' in complex_num:
        real_part, imag_part = map(float, complex_num.split('+'))
        imag_part = imag_part[:-1]
    else:
        real_part = float(complex_num)
        imag_part = 0
        if 'j' not in complex_num:
            continue
    if complex_num[-1] == 'j':
        if complex_num[0] == '-':
            coeff = -1
        elif '+' in complex_num:
            coeff = 1
        else:
            coeff = 1 if imag_part != 0 else 0
        imag_part = coeff * float(imag_part[:-1])
    result_dict[real_part] = coeff

print(result_dict)