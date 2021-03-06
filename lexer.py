TOK_FN = 101
TOK_LET = 102
TOK_IF = 103
TOK_FOR = 104
TOK_WHILE = 105
TOK_ID = 1
TOK_CHAR = 2
TOK_EQ = 3
TOK_BIGGER = 4
TOK_SMALLER = 5
TOK_NOT = 6
TOK_NUM = 7


class Token:

    def __init__(self, token_id, data):
        self.token_id = token_id
        self.data = data

    def __repr__(self):
        rep = 'Token(' + str(self.token_id) + ',' + self.data + ')'
        return rep

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.token_id == other.token_id and \
                   self.data == other.data
        else:
            return False


def tokenize(data):
    keywords = ['fn', 'let', 'if', 'for', 'while']
    id_alphabet = '0123456789_abcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'
    res = []
    data_list = data.split()

    for key in data_list:
        if key == 'fn':
            res.append(Token(TOK_FN, key))
        elif key == 'let':
            res.append(Token(TOK_LET, key))
        elif key == 'if':
            res.append(Token(TOK_IF, key))
        elif key == 'for':
            res.append(Token(TOK_FOR, key))
        elif key == 'while':
            res.append(Token(TOK_WHILE, key))
        elif key == '==':
            res.append(Token(TOK_EQ, key))
        elif key == '>=':
            res.append(Token(TOK_BIGGER, key))
        elif key == '<=':
            res.append(Token(TOK_SMALLER, key))
        elif key == '!=':
            res.append(Token(TOK_NOT, key))

        elif key not in keywords:
            state = 1
            id_name = ''
            is_char = False

            for char in key:
                if state == 1:
                    if char in '0123456789':
                        return None
                    elif char in id_alphabet:
                        id_name += char
                        state = 2
                    else:                       # CHARS
                        id_name += char
                        state = 1
                        is_char = True
                elif state == 2:
                    if char in id_alphabet:
                        id_name += char
                        state = 2
                    else:
                        return id_name

            if is_char is True:
                res.append(Token(TOK_CHAR, id_name))
            else:
                res.append(Token(TOK_ID, id_name))

            # state = 1
            # id_name = ''
    return res


if __name__ == '__main__':
    print(tokenize('if a = b let data jhc1_1'))
