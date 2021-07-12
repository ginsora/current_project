def word(data):
    list1 = ['fn', 'let', 'if', 'for', 'while']
    res = []

    for char in data:
        if char in list1 and char == 'fn':
            res.append(101)
        elif char in list1 and char == 'let':
            res.append(102)
        elif char in list1 and char == 'if':
            res.append(103)
        elif char in list1 and char == 'for':
            res.append(104)
        elif char in list1 and char == 'while':
            res.append(105)
    return res


if __name__ == '__main__':
    #print(word('if let for while'))
    print(word(['fn', 'let', 'for']))
