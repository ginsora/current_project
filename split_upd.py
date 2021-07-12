def check(char):
    return char in ' '


def my_split(data):
    res = ''
    res_fin = []
    i = 0

    for char in data:
        if check(char):
            res_fin.append(res)
            res = ''
        else:
            res += char
        i += 1
        if i == len(data):
            res_fin.append(res)
    return res_fin


if __name__ == '__main__':
    print(my_split('if let for while'))
    print(my_split('hello world'))
