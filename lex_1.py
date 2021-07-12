TOK_FN = 101
TOK_LET = 102
TOK_IF = 103
TOK_FOR = 104
TOK_WHILE = 105


def word(data):
    keywords = ['fn', 'let', 'if', 'for', 'while']
    res = []
    dataList = data.split()

    for char in dataList:
        if char in keywords and char == 'fn':
            res.append(TOK_FN)
        elif char in keywords and char == 'let':
            res.append(TOK_LET)
        elif char in keywords and char == 'if':
            res.append(TOK_IF)
        elif char in keywords and char == 'for':
            res.append(TOK_FOR)
        elif char in keywords and char == 'while':
            res.append(TOK_WHILE)
    return res


if __name__ == '__main__':
    print(word('if let for while'))
    #print(word(['fn', 'let', 'for']))
