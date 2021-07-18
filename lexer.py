TOK_FN = 101
TOK_LET = 102
TOK_IF = 103
TOK_FOR = 104
TOK_WHILE = 105


class Token:

    def __init__(self, token_id, data):
        self.token_id = token_id
        self.data = data

    def __repr__(self):
        rep = 'Token(' + str(self.token_id) + ',' + self.data + ')'
        return rep


def check(char):
    return char in '0123456789_abcdefjhijklmnopqrstuvwxyz'


def tokenize(data):
    keywords = ['fn', 'let', 'if', 'for', 'while']
    res = []
    data_list = data.split()
    state = 1
    res1 = ''

    for key in data_list:
        if key in keywords and key == 'fn':
            res.append(Token(TOK_FN, 'fn'))
        elif key in keywords and key == 'let':
            res.append(Token(TOK_LET, 'let'))
        elif key in keywords and key == 'if':
            res.append(Token(TOK_IF, 'if'))
        elif key in keywords and key == 'for':
            res.append(Token(TOK_FOR, 'for'))
        elif key in keywords and key == 'while':
            res.append(Token(TOK_WHILE, 'while'))
        elif key == '==':
            res.append(Token(3, key))
        elif key == '>=':
            res.append(Token(4, key))
        elif key == '<=':
            res.append(Token(5, key))
        elif key == '!=':
            res.append(Token(6, key))

        elif key != keywords:

            for char in key:
                if state == 1:
                    if char in '0123456789':
                        raise AssertionError('Error')
                    elif check(char):
                        res1 += char
                        state = 2
                    ''' else:
                        res1 += char
                        res.append(Token(2, res1))
                        state = 1 '''
                elif state == 2:
                    if check(char):
                        res1 += char
                        state = 2
                    else:
                        return res1

            res.append(Token(1, res1))  # !!!!!
            state = 1
            res1 = ''
    return res


if __name__ == '__main__':
    print(tokenize('if a = b let data jhc1_1'))
