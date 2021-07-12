def check(char):
    return char in '0123456789'


def get_digit(data):
    state = 12
    res = ' '

    for char in data:
        if state == 12:
            if check(char):
                res += char
                state = 13
            else:
                raise AssertionError('Error')
        elif state == 13:
            if check(char):
                res += char
                state = 13
            elif char == '.':
                res += char
                state = 14
            elif char == 'E':
                res += char
                state = 16
            else:
                state = 20
        elif state == 14:
            if check(char):
                res += char
                state = 15
            else:
                raise AssertionError('Error')
        elif state == 15:
            if check(char):
                res += char
                state = 15
            elif char == 'E':
                res += char
                state = 16
            else:
                state = 21
        elif state == 16:
            if char == '+' or '-':
                res += char
                state = 17
            elif check(char):
                res += char
                state = 18
            else:
                raise AssertionError('Error')
        elif state == 17:
            if check(char):
                res += char
                state = 18
            else:
                raise AssertionError('Error')
        elif state == 18:
            if check(char):
                res += char
                state = 18
            else:
                state = 19
        elif state == 19 or 20 or 21:
            return res
        else:
            raise AssertionError('Error')

    return res


if __name__ == '__main__':
    print(get_digit('10.8E+5'))
    print(get_digit('100.9EE+9'))